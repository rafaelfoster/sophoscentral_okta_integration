#!/usr/bin/python3

import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
packages_path = "%s/%s" % (dir_path, "packages")
vendors_path = "%s/%s" % (dir_path, "vendors")
sys.path.insert(0,packages_path)
sys.path.insert(0,vendors_path)

import time
import asyncio
import logging
import requests
import argparse as ap

from mwt import mwt
from os import path     
from re import match
from vendors.sophos_central.sophos_auth import Auth
from vendors.sophos_central.sophos_users import User
from vendors.okta.client import Client as OktaClient
from config import sophos_central_api_config as api_conf

def get_file_location(process_path):
    dir_name = path.dirname(path.abspath(__file__))
    final_path = "{0}{1}".format(dir_name, process_path)
    return final_path

async def okta_getUsers(okta_client):
    query_param = {'limit': '5'}
    users, resp, err = await okta_client.list_users(query_param)
#    print(err)
#    print(resp)
    # print(users)
    okta_users = list()
    
    if users is not None:
        for user in users:
            temp_user = dict()
            temp_user["name"]      = "Nubank - %s %s" % (user.profile.first_name,user.profile.last_name)
            temp_user["email"]     = user.profile.email
            temp_user["lastName"]  = user.profile.last_name
            temp_user["firstName"] = user.profile.first_name
            okta_users.append(temp_user)

    return okta_users

#    groups, resp, err = await okta_client.list_groups()
#    for group in groups:
#        print(group)
#        print(group.profile.name)
#        print(group)
#        break

def main():
    user = User()
    auth = Auth()
    credentials_path = api_conf.credentials_path
    credentails_real_path = get_file_location(credentials_path)
    
    auth_url = api_conf.auth_uri
    users_uri = api_conf.users_uri
    whoami_url = api_conf.whoami_uri

    sophos_client_id = auth.load_credentials(credentails_real_path, "sophos_central", "client_id")
    sophos_client_secret = auth.load_credentials(credentails_real_path, "sophos_central", "client_secret")
    
    okta_url   = auth.load_credentials(credentails_real_path, "okta", "orgUrl")
    okta_token = auth.load_credentials(credentails_real_path, "okta", "token")

    sophos_access_token = auth.get_token(sophos_client_id, sophos_client_secret, auth_url)

    headers = auth.valid_headers(sophos_access_token)

    tenant_data = auth.get_tentant(headers, whoami_url)
    central_dataregion = tenant_data["apiHosts"]["dataRegion"]

    headers["X-Tenant-ID"] = tenant_data['id']
    user.setHeaders(headers)
    
    Users_URL = "{DATA_REGION}/{USERS_URI}".format(DATA_REGION=central_dataregion, USERS_URI=users_uri)

    print("Getting list of Sophos Central Users..")
    Central_Users = user.get_all_users(Users_URL)
    print("Done!")
    
    config = {
        'orgUrl': okta_url,
        'token': okta_token
    }
    okta_client = OktaClient(config)

    loop = asyncio.get_event_loop()
    okta_users = loop.run_until_complete(okta_getUsers(okta_client))
    
    for user_data in okta_users:
    
        if not any(d['email'] == user_data["email"] for d in Central_Users["items"]):
             print("User %s does not exist.... Creating it..." % (user_data["name"]) )
             create_users = user.create(Users_URL, user_data)
             print("Central User ID: %s " % (create_users["id"]) )
        else:
             print("User %s already exist! Skipping" % (user_data['name']) )

        Central_Users = user.get_all_users(Users_URL)

if __name__ == "__main__":
    main()

