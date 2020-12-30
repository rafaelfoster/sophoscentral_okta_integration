import json
import time
import logging
import requests
import argparse as ap
from config import sophos_central_api_config as api_conf

from mwt import mwt
from os import path     
from re import match
from sophos_central.sophos_auth import Auth
from sophos_central.sophos_users import User

def lambda_handler(event, context):
    main()

def get_file_location(process_path):
    dir_name = path.dirname(path.abspath(__file__))
    final_path = "{0}{1}".format(dir_name, process_path)
    return final_path

def main():
    user = User()
    auth = Auth()
    sophos_conf_path = api_conf.sophos_conf_path
    sophos_final_path = get_file_location(sophos_conf_path)
    
    auth_url = api_conf.auth_uri
    users_uri = api_conf.users_uri
    whoami_url = api_conf.whoami_uri

    client_id, client_secret = auth.load_credentials(sophos_final_path)

    sophos_access_token = auth.get_token(client_id, client_secret, auth_url)


    headers = auth.valid_headers(sophos_access_token)


    tenant_data = auth.get_tentant(headers, whoami_url)
    central_dataregion = tenant_data["apiHosts"]["dataRegion"]

    headers["X-Tenant-ID"] = tenant_data['id']
    user.setHeaders(headers)
    
    Users_URL = "{DATA_REGION}/{USERS_URI}".format(DATA_REGION=central_dataregion, USERS_URI=users_uri)

    start = time.time()
    Central_Users = user.get_all_users(Users_URL)
    end = time.time()
    #print("\n\n Not cached execution time: ")
    #print(end - start)


    # A single user for testing purposes.
    # user_data should be filled with OKTA user from its API
    #user_data = dict()
    #user_data["name"] = "TEST USER"
    #user_data["email"] = "testing@rafaelfoster.com.br"

    if not any(d['email'] == user_data["email"] for d in Central_Users["items"]):
         print("User does not exist.... Creating user...")
         create_users = user.create(Users_URL, user_data)
         print(create_users)
    else:
         print("user exist! Skipping")


    start = time.time()
    Central_Users = user.get_all_users(Users_URL)
    end = time.time()
    # print("\n\nCached execution time: ")
    # print(end - start)
    # print("\n\n")
    # print(Central_Users)
