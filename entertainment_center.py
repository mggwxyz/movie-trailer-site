import media
import fresh_tomatoes
import movie_api

# Instatiant movie list
movie_list = []

# Add movies to movie list
movie_list = movie_api.get_popular_movies()

# Open up list of movies
fresh_tomatoes.open_movies_page(movie_list)