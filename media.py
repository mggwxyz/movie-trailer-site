"""Module for media classes and objects like Movie"""


class Movie:
    """A class to represent movies"""
    def __init__(self, title, overview, poster_image_url, trailer_youtube_url):
        self.title = title
        self.overview = overview
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
