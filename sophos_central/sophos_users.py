import requests
from mwt import mwt

class User(object):

    headers = ""

    def setHeaders(self, headers):
        self.headers = headers

    @mwt(timeout=60*60) 
    def get_all_users(self, users_url):
        headers = self.headers
        
        params_data = {}
        params_data["fields"] = []
        params_data["fields"].append("name")
        params_data["fields"].append("email")

        params_data["search"] = []
        params_data["search"].append("@")

        params_data["searchFields"] = []
        params_data["searchFields"].append("email")
        
        try:
            res_users = requests.get(users_url, headers=headers, params=params_data)
            res_users_code = res_users.status_code
            users_data = res_users.json()
           
        except requests.exceptions.RequestException as res_exception:
            res_users_error_code = users_data['error']
            return res_users_error_code
        
        if res_users_code == 200:
            return users_data
    

    def create(self, users_url, user_data):
        try:
            headers = self.headers
            user_info = "name={0}&email={1}".format(user_data["name"], user_data["email"])
            res = requests.post(users_url, headers=headers, json=user_data)
            res_code = res.status_code
            res_data = res.json()

        except requests.exceptions.RequestException as res_exception:
            res_users_error_code = res_data['error']
            return res_users_error_code

        if res_code == 200:
            return res_data
        
