import requests
import media

TMDB_KEY = '4f9ab9ab6f23cfad18b769caedf78b8d'
BASE_URL = 'https://api.themoviedb.org/3'
YT_BASE_URL = 'https://www.youtube.com/watch?v='


def get_popular_movies():
    SP = {'api_key': TMDB_KEY, 'sort_by': 'popularity.desc'}
    VP = {'api_key': TMDB_KEY, 'append_to_response': 'videos'}

    # Search for a list of the most popular movies
    S_RESPONSE = requests.get(BASE_URL + '/discover/movie', params=SP)
    popular_movie_list = S_RESPONSE.json()

    # Query for each movies trailer
    for result in popular_movie_list['results']:
        movie_id = result['id']
        VR = requests.get(BASE_URL + '/movie/' + str(movie_id), params=VP)
        video_json = VR.json()
        # Search through the video results for YouTube trailer
        if('videos' in video_json):
            for video_result in video_json['videos']['results']:
                has_trailer = video_result['type'] == 'Trailer'
                from_youtube = video_result['site'] == 'YouTube'
                if(has_trailer and from_youtube):
                    video_url = YT_BASE_URL + video_result['key']
                    result['trailer_youtube_url'] = video_url
                    break
    movie_list = []
    poster_base_url = 'https://image.tmdb.org/t/p/w185'

    # Convert result into list of Movie objects
    for movie in popular_movie_list['results']:
        if 'trailer_youtube_url' in movie:
            # Get movie values from item in list
            title = movie['title']
            overview = movie['overview']
            poster = poster_base_url + movie['poster_path']
            trailer = movie['trailer_youtube_url']

            # Create Movie and add it to the movie list to be returned
            new_movie = media.Movie(title, overview, poster, trailer)
            movie_list.append(new_movie)

    return movie_list

get_popular_movies()
