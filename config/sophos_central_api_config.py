from pathlib import PurePath

# Static URI Variables
auth_uri = 'https://id.sophos.com/api/v2/oauth2/token'
whoami_uri = 'https://api.central.sophos.com/whoami/v1'
users_uri = '/common/v1/directory/users'

# Path locations
sophos_conf_path = PurePath("/config/sophos_config.ini")
intelix_conf_path = PurePath("/config/intelix_config.ini")
