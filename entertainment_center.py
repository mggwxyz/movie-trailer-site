"""Module for launching movie website"""

import fresh_tomatoes
import movie_api

# Instantiate movie list
MOVIE_LIST = []

# Add movies to movie list
MOVIE_LIST = movie_api.get_popular_movies()

# Open up list of movies
fresh_tomatoes.open_movies_page(MOVIE_LIST)
