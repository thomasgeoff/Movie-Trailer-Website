# Imports fresh_tomatoes and media
import fresh_tomatoes
import media

"""Created 8 Movie class objects, initialized with
   Movie Title,Movie Type&Year,Movie Storyline,Movie Poster,
   Movie Rating,Movie Trailer information"""

# Movie class objects
toy_story = media.Movie("Toy Story",
                        "1995.Fantasy/Adventure",
                        "A story of a boy and his toys that come to life",
                        "https://goo.gl/XroMgC",
                        "IMDB: 8.3/10",
                        "https://youtu.be/KYz2wyBy3kc")

fast8 = media.Movie("Fate of the Furious",
                    "2017.Crime film/Thriller",
                    "Dom's family couldn't maintain peasce for long",
                    "https://goo.gl/4WJ9Mu",
                    "IMDB: 6.7/10",
                    "https://youtu.be/iUhJAjnCY8Y")

crazy_stupid_love = media.Movie("Crazy,Stupid,Love",
                                "2011.Comedy-drama/Drama",
                                "A divorced man rediscovers his manhood.",
                                "https://goo.gl/VEoU4j",
                                "IMDB: 7.4/10",
                                "https://youtu.be/aDLhjm-0rJQ")

ugly_truth = media.Movie("Ugly Truth",
                         "2009.Romance/Comedy",
                         "Life of a Romantically challenged show producer",
                         "https://goo.gl/YtJaC3",
                         "IMDB: 6.9/10",
                         "https://youtu.be/DvsZtGxsvV0")

this_means_war = media.Movie("This Means War",
                             "2012.Action/Romance",
                             "Two CIA agents dates the same woman.",
                             "https://goo.gl/ohFKk2",
                             "IMDB: 6.3/10",
                             "https://youtu.be/oleuD8479uM")

boyka_undisputed = media.Movie("Boyka: Undisputed",
                               "2017.Drama/Crime film",
                               "Life of an underground fighter.",
                               "https://goo.gl/AfoPrK",
                               "IMDB: 7.1/10",
                               "https://youtu.be/KQtB3-NMfnU")

doctor_strange = media.Movie("Doctor Strange",
                             "2016.Fantasy/Science fiction film",
                             "An accident changes Dr. Stephen Strange's life",
                             "https://goo.gl/syGA1w",
                             "IMDB: 7.5/10",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

lucky_one = media.Movie("The Lucky One",
                        "2012.Drama/Romance",
                        "U.S. Marine returns home with a belief.",
                        "https://goo.gl/2avkWz",
                        "IMDB: 6.5/10",
                        "https://www.youtube.com/watch?v=9w8lE83oYeM")

# Stores all the Movie instances in a list
movies = [boyka_undisputed, crazy_stupid_love, doctor_strange, fast8,
          lucky_one, this_means_war, toy_story, ugly_truth]

# Creates an HTML file and displays all the movie instances as a webpage
fresh_tomatoes.open_movies_page(movies)
