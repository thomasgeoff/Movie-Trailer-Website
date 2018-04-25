# Imports the webbrowser module
import webbrowser


class Movie():
    """This class provides a way to store movie related information like:
       Movie Title
       Movie Type&Year
       Movie Storyline
       Movie Poster
       Movie Rating
       Movie Trailer"""
# Function that initialises Movie class instance variables
    def __init__(self, movie_title, movie_type_year, movie_storyline,
                 poster_image, rating, trailer_youtube):
            self.title = movie_title
            self.type_year = movie_type_year
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.movie_rating = rating
            self.trailer_youtube_url = trailer_youtube

# Function to play the movie trailer
    def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
