import media
import fresh_tomatoes

# Instatiant movie list
movie_list = []

# Add movies to movie list
movie_list.append(media.Movie('Interstellar', 'https://image.tmdb.org/t/p/original//nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg', 'https://www.youtube.com/watch?v=1V6_lHq2chE'))
movie_list.append(media.Movie('The Sandlot', 'https://image.tmdb.org/t/p/original/fKJUQrAm5QbVR5DqgH9U5IflHGQ.jpg', 'https://www.youtube.com/watch?v=ec9W8JbFykw'))
movie_list.append(media.Movie('Forrest Gump', 'https://image.tmdb.org/t/p/original/yE5d3BUhE8hCnkMUJOo1QDoOGNz.jpg', 'https://www.youtube.com/watch?v=bLvqoHBptjg'))
movie_list.append(media.Movie('Spaceballs', 'https://image.tmdb.org/t/p/original/kNbaxEsnCyWBTfANVPHayujBsxp.jpg', 'https://www.youtube.com/watch?v=WZsVNkx7NLw'))
movie_list.append(media.Movie('Ex Machina', 'https://image.tmdb.org/t/p/original/btbRB7BrD887j5NrvjxceRDmaot.jpg', 'https://www.youtube.com/watch?v=bggUmgeMCdc'))
movie_list.append(media.Movie('Hot Tub Time Machine', 'https://image.tmdb.org/t/p/original/zERxFAXiQdPAfsumIIcBFH8fOVt.jpg', 'https://www.youtube.com/watch?v=561ouGGhR64'))

# Open up list of movies
fresh_tomatoes.open_movies_page(movie_list)