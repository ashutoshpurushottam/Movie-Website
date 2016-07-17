import requests
import tmdbsimple as tmdb
import media
import fresh_tomatoes

# Get request token from the moviedb
API_KEY = "16e06503367744093ba784c46dc0fc9c"
tmdb.API_KEY = API_KEY
BASE_URL_SECURE_STRING = "https://api.themoviedb.org/3/"
GET_TOKEN_METHOD = "authentication/token/new"
LOGIN_METHOD = "authentication/token/validate_with_login"
GET_SESSION_ID_METHOD = "authentication/session/new"
GET_ACCOUNT_INFO_METHOD = "account"
# URLs for trailer and posters for movie objects
YOUTUBE_BASE_URL = 'https://www.youtube.com/watch?v='
TMDB_POSTER_BASE_URL = 'http://image.tmdb.org/t/p/w500/'
user_name = "apurushottam"
password = "ashi1807"



def get_request_token():
    url_string = BASE_URL_SECURE_STRING + GET_TOKEN_METHOD + "?api_key=" + API_KEY
    r = requests.get(url_string)
    config = r.json()
    token = config['request_token']
    return token

def authenticate_token():
    token = get_request_token()
    parameters = "?api_key=" + API_KEY + "&request_token=" + token + "&username=" + user_name + "&password=" + password
    url_string = BASE_URL_SECURE_STRING + LOGIN_METHOD + parameters
    r = requests.get(url_string)
    return token


def get_session_id():
    token = authenticate_token()
    parameters = "?api_key=" + API_KEY + "&request_token=" + token
    url_string = BASE_URL_SECURE_STRING + GET_SESSION_ID_METHOD + parameters
    r = requests.get(url_string)
    response_json = r.json()
    session_id = response_json['session_id']
    return session_id, token


def get_account_id():
    session_id, token = get_session_id()
    parameters = "?api_key=" + API_KEY + "&session_id=" + session_id
    url_string = BASE_URL_SECURE_STRING + GET_ACCOUNT_INFO_METHOD + parameters
    r = requests.get(url_string)
    response_json = r.json()
    user_id = response_json['id']
    return user_id, session_id

def get_favorite_movies_ids():
    user_id, session_id = get_account_id()
    get_favorite_movies_method = "account/{id}/favorite/movies"
    get_favorite_movies_method = get_favorite_movies_method.format(id=user_id)
    parameters = "?api_key=" + API_KEY + "&session_id=" + session_id
    url_string = BASE_URL_SECURE_STRING + get_favorite_movies_method + parameters
    r = requests.get(url_string)
    response_json = r.json()
    movies_array = response_json['results']
    id_list = []
    for movie in movies_array:
        id_list.append(movie['id'])
    print id_list
    return id_list

# declare movies list to hold favorite movies for the user
movies_list = []

# construct movie objects for each id and append in movies list
for id in get_favorite_movies_ids():
    # Construct avatar trailer url
    movie_videos = tmdb.Movies(id).videos()
    movie_video = movie_videos['results'][0]
    movie_trailer_url = YOUTUBE_BASE_URL + movie_video['key']

    # Construct title, overview and poster for avatar
    movie_info = tmdb.Movies(id).info()
    movie_title = movie_info['title']
    movie_overview = movie_info['overview']
    movie_poster_url = TMDB_POSTER_BASE_URL + movie_info['poster_path']

    # Construct avatar movie object
    movie = media.Movie(movie_title, movie_overview, movie_poster_url, movie_trailer_url)
    movies_list.append(movie)


fresh_tomatoes.open_movies_page(movies_list)
