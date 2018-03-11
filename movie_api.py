"""
This module gets the movie lists from The Movie Database
"""

import requests
import pprint
import media

TMDB_KEY = '4f9ab9ab6f23cfad18b769caedf78b8d'
BASE_URL = 'https://api.themoviedb.org/3'

def get_popular_movies():
    SEARCH_PAYLOAD = { 'api_key': TMDB_KEY, 'sort_by': 'popularity.desc' }
    VIDEO_SEARCH_PAYLOAD = { 'api_key': TMDB_KEY, 'append_to_response': 'videos' }

    # Search for a list of the most popular movies
    SEARCH_RESPONSE = requests.get(BASE_URL + '/discover/movie', params=SEARCH_PAYLOAD)
    popular_movie_list = SEARCH_RESPONSE.json()

    # For each popular movie in the list, query for the videos related to that movie
    for result in popular_movie_list['results']:
        movie_id = result['id']
        VIDEO_RESPONSE = requests.get(BASE_URL + '/movie/' + str(movie_id), params=VIDEO_SEARCH_PAYLOAD)
        video_json = VIDEO_RESPONSE.json()
        # Search through the video results and find video that is a trailer on YouTube
        if('videos' in video_json):
            for video_result in video_json['videos']['results']:
                if(video_result['site'] == 'YouTube' and video_result['type'] == 'Trailer'):
                    video_url = 'https://www.youtube.com/watch?v=' + video_result['key']
                    result['trailer_youtube_url'] = video_url
                    print(result)
                    break
    movie_list = []

    # Convert result into list of Movie objects
    for movie in popular_movie_list['results']:
        pprint.pprint(movie)
        if 'trailer_youtube_url' in movie:
            movie_list.append(media.Movie(movie['title'], 'https://image.tmdb.org/t/p/w185' + movie['poster_path'], movie['trailer_youtube_url']))           

    return movie_list

get_popular_movies()
