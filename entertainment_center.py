# Imports
import tmdbsimple as tmdb
tmdb.API_KEY = '16e06503367744093ba784c46dc0fc9c'
import media
import fresh_tomatoes

# URLs for trailer and posters for movie objects
YOUTUBE_BASE_URL = 'https://www.youtube.com/watch?v='
TMDB_POSTER_BASE_URL = 'http://image.tmdb.org/t/p/w500/'

# Create instance of six favorite movies

# Construct avatar trailer url
avatar_videos = tmdb.Movies(19995).videos()
avatar_video = avatar_videos['results'][0]
avatar_trailer_url = YOUTUBE_BASE_URL +  avatar_video['key']

# Construct title, overview and poster for avatar
avatar_info = tmdb.Movies(19995).info()
avatar_title = avatar_info['title']
avatar_overview = avatar_info['overview']
avatar_poster_url = TMDB_POSTER_BASE_URL + avatar_info['poster_path']

# Construct avatar movie object
avatar = media.Movie(avatar_title, avatar_overview, avatar_poster_url, avatar_trailer_url)

# Construct creed trailer url
creed_videos = tmdb.Movies(312221).videos()
creed_video = creed_videos['results'][0]
creed_trailer_url = YOUTUBE_BASE_URL + creed_video['key']

# Construct title, overview and poster for creed
creed_info = tmdb.Movies(312221).info()
creed_title = creed_info['title']
creed_overview = creed_info['overview']
creed_poster_url = TMDB_POSTER_BASE_URL + creed_info['poster_path']

# Create creed object
creed = media.Movie(creed_title, creed_overview, creed_poster_url, creed_trailer_url)

# Construct interstellar trailer url
interstellar_videos = tmdb.Movies(157336).videos()
interstellar_video = interstellar_videos['results'][0]
interstellar_trailer_url = YOUTUBE_BASE_URL +  interstellar_video['key']

# Construct title, overview and poster for interstellar
interstellar_info = tmdb.Movies(157336).info()
interstellar_title = interstellar_info['title']
interstellar_overview = interstellar_info['overview']
interstellar_poster_url = TMDB_POSTER_BASE_URL + interstellar_info['poster_path']

# Construct interstellar movie object
interstellar = media.Movie(interstellar_title, interstellar_overview, interstellar_poster_url, interstellar_trailer_url)

# Construct titanic trailer url
titanic_videos = tmdb.Movies(597).videos()
titanic_video = titanic_videos['results'][0]
titanic_trailer_url = YOUTUBE_BASE_URL +  titanic_video['key']

# Construct title, overview and poster for titanic
titanic_info = tmdb.Movies(597).info()
titanic_title = titanic_info['title']
titanic_overview = titanic_info['overview']
titanic_poster_url = TMDB_POSTER_BASE_URL + titanic_info['poster_path']

# Construct titanic movie object
titanic = media.Movie(titanic_title, titanic_overview, titanic_poster_url, titanic_trailer_url)

# Construct con air trailer url
conair_videos = tmdb.Movies(1701).videos()
conair_video = conair_videos['results'][0]
conair_trailer_url = YOUTUBE_BASE_URL +  conair_video['key']

# Construct title, overview and poster for con air
conair_info = tmdb.Movies(1701).info()
conair_title = conair_info['title']
conair_overview = conair_info['overview']
conair_poster_url = TMDB_POSTER_BASE_URL + conair_info['poster_path']

# Construct con air movie object
conair = media.Movie(conair_title, conair_overview, conair_poster_url, conair_trailer_url)

# Construct insidious trailer url
insidious_videos = tmdb.Movies(49018).videos()
insidious_video = insidious_videos['results'][0]
insidious_trailer_url = YOUTUBE_BASE_URL +  insidious_video['key']

# Construct title, overview and poster for insidiuos
insidious_info = tmdb.Movies(49018).info()
insidious_title = insidious_info['title']
insidious_overview = insidious_info['overview']
insidious_poster_url = TMDB_POSTER_BASE_URL + insidious_info['poster_path']

# Construct insidious movie object
insidious = media.Movie(insidious_title, insidious_overview, insidious_poster_url, insidious_trailer_url)


movies = [avatar, titanic, creed, interstellar, conair, insidious]
fresh_tomatoes.open_movies_page(movies)
