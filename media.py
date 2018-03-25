"""Module for media classes and objects like Movie"""

class Movie:
    """A class to represent movies
    
    This class contains the __init__ function of movie class instances
    
    Attributes
    ----------
    title : str
        The title of the movie
    overview : str 
        The overview describing the movie
    poster_image_url : str
        The url for the image of the movie's poster
    trailer_youtube_url : str
        The url slug for the movie's youtube trailer
        
    Parameters
    ----------
    title : str
        The title of the movie
    overview : str 
        The overview describing the movie
    poster_image_url : str
        The url for the image of the movie's poster
    trailer_youtube_url : str
        The url slug for the movie's youtube trailer
            
    """
    
    def __init__(self, title, overview, poster_image_url, trailer_youtube_url):
        self.title = title
        self.overview = overview
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
