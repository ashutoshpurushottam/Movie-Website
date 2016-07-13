import requests

# 1. Get request token from the moviedb
api_key = "16e06503367744093ba784c46dc0fc9c"
base_url_secure_string = "https://api.themoviedb.org/3/"
get_token_method = "authentication/token/new"
login_method = "authentication/token/validate_with_login"
get_session_id_method = "authentication/session/new"
get_account_info_method = "account"
user_name = "apurushottam"
password = "ashi1807"

def get_request_token():
    url_string = base_url_secure_string + get_token_method + "?api_key=" + api_key
    r = requests.get(url_string)
    config = r.json()
    token = config['request_token']
    return token

def authenticate_token():
    token = get_request_token()
    parameters = "?api_key=" + api_key + "&request_token=" + token + "&username=" + user_name + "&password=" + password
    url_string = base_url_secure_string + login_method + parameters
    r = requests.get(url_string)
    return token


def get_session_id():
    token = authenticate_token()
    parameters = "?api_key=" + api_key + "&request_token=" + token
    url_string = base_url_secure_string + get_session_id_method + parameters
    r = requests.get(url_string)
    response_json = r.json()
    session_id = response_json['session_id']
    return session_id, token


def get_account_id():
    session_id, token = get_session_id()
    parameters = "?api_key=" + api_key + "&session_id=" + session_id
    url_string = base_url_secure_string + get_account_info_method + parameters
    r = requests.get(url_string)
    response_json = r.json()
    user_id = response_json['id']
    return user_id, session_id

def get_favorite_movies():
    user_id, session_id = get_account_id()
    get_favorite_movies_method = "account/{id}/favorite/movies"
    get_favorite_movies_method = get_favorite_movies_method.format(id=user_id)
    parameters = "?api_key=" + api_key + "&session_id=" + session_id
    url_string = base_url_secure_string + get_favorite_movies_method + parameters
    r = requests.get(url_string)
    response_json = r.json()
    movies_array = response_json['results']
    print movies_array
    return movies_array

get_favorite_movies()

