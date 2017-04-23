import fresh_tomatoes
import media
# Here we will insatntiate five movies of the class movie with all their
# corresponding informations
toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story about a marine goes to an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://youtu.be/5PSNL1qE6VY")

hidden_figures = media.Movie("Hidden Figures", "A story of three black women"
                             "succeeded in NASA despite all the challenges",
                             "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",  # NOQA
                             "https://youtu.be/RK8xHq6dfAo")

beautiful_mind = media.Movie("A Beautiful Mind", " A story of a great"
                             "mathmatisian who suffered of a mental disease",
                             "https://upload.wikimedia.org/wikipedia/sco/b/b8/A_Beautiful_Mind_Poster.jpg",  # NOQA
                             "https://youtu.be/YWwAOutgWBQ")

gifted_hands = media.Movie("Gifted Hand",
                           "A story of an ordinary boy becomes a great surgeon"
                           "because of his mother's encouragement",
                           "https://upload.wikimedia.org/wikipedia/en/1/15/Gifted-hands-movie.jpg",  # NOQA
                           "https://youtu.be/AmiDwytfvbA")

mulan = media.Movie("Mulan", "A story about an ordinary girl who saved china",
                    "https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",  # NOQA
                    "https://youtu.be/wAbGAkkOgcM")

movies = [toy_story, avatar, hidden_figures, beautiful_mind,
          gifted_hands, mulan]
# Create a list of all the instances(movies)
fresh_tomatoes.open_movies_page(movies)
# Pass the created list to the function open_movies_page()in fresh_tomatoes.py
# module which is created by Udacity to create an html page with all the movies
# on the list
