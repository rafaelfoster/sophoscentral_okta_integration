import requests
import configparser as cp

class Auth(object):
        
    def load_credentials(self, sophos_final_path, section, parameter):
        sophos_conf = cp.ConfigParser(allow_no_value=True)
        sophos_conf.read(sophos_final_path)
        return sophos_conf.get(section, parameter)
        

    def get_token(self, client_id, client_secret, auth_url):
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data_tok = "grant_type=client_credentials&client_id={0}&client_secret={1}&scope=token".format(client_id,
                                                                                                          client_secret)
            res = requests.post(auth_url, headers=headers, data=data_tok)
            res_code = res.status_code
            res_data = res.json()
            if res_code == 200:
                sophos_access_token = res_data['access_token']
                return sophos_access_token
            else:
                res_error_code = res_data['errorCode']
                res_message = "Response Code: {0} Message: {1}".format(res_code, res_data['message'])
                return None, res_message, res_error_code
        

    def valid_headers(self, sophos_access_token):
            if sophos_access_token[0] is not None:
                headers = {"Authorization": "Bearer {0}".format(sophos_access_token), "Accept": "application/json"}
                return headers
            else:
                exit(1)
        

    def get_tentant(self, headers, whoami_url):
            try:
                res_tenant = requests.get(whoami_url, headers=headers)
                res_tenant_code = res_tenant.status_code
                tenant_data = res_tenant.json()
            except requests.exceptions.RequestException as res_exception:
                print("Failed to obtain the tenant ID")
                res_tenant_error_code = tenant_data['error']
                print(res_exception)
                print("Err Code: {0}, Err Detail: {1}".format(res_tenant_code, res_tenant_error_code))
                exit(1)
            if res_tenant_code == 200:
                return tenant_data