import webbrowser


class Movie():
    # This class will hold some informations about you favourite movie

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        # The function show_trailer opens the movie trailer URL on youtube
        webbrowser.open(self.trailer)
