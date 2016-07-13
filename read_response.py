
import requests
from urllib2 import Request, urlopen

def get_request_token():
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/authentication/token/new?api_key={key}'
    KEY = '16e06503367744093ba784c46dc0fc9c'
    request_token_url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(request_token_url)
    config = r.json()
    request_token = config['request_token']
    return request_token

request_token = get_request_token()

def get_session_id():
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/authentication/session/new?api_key={key}'
    KEY = '16e06503367744093ba784c46dc0fc9c'
    session_id_url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(session_id_url)
    config = r.json()
    print config

get_session_id()



