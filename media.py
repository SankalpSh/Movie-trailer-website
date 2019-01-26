import webbrowser


class Movie():
    """The program provides information regarding movies
       def __init__(args) initializes variables
       eg- arg (self.movie_titles = movie-titles)
       will recieve the movie title.
       """
    VALID_RATING = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):  # noqa

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """"The Functional Docstring """
        webbrowser.open(self.trailer_youtube_url)
