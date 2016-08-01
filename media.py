# Stage 3: Movies Website

import webbrowser

class Movie():
    """ This class provides a way to store movie related information."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date, running_time, movie_genre):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = release_date
        self.time = running_time
        self.genre = movie_genre

    def show_trailer(self):
        # Open a webbrowser to play a YouTube video.
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        # Open a webbrowser to display a poster image.
        webbrowser.open(self.poster_image_url)
        