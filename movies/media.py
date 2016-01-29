import webbrowser


class Movie:
    """Implements a container for movie data"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_year, stars):
        """Assign movie information from parameters"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year
        self.stars = stars

    def show_trailer(self):
        """Open a new browser window and show the youtube
        trailer for this movie instance"""

        webbrowser.open(self.trailer_youtube_url)
