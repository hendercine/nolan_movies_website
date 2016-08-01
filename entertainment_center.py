# Stage 3: Movies Website

import media
import fresh_tomatoes

# The following are instances of class Movie as defined in the media.py file.
# The order in which each string is placed corresponds with the order of these
#    instances: movie_title, movie_storyline, poster_image,
#                 trailer_youtube, release_date, running_time, movie_genre.

following = media.Movie("Following",
                        "A young writer who follows strangers for material meets a thief who takes him under his wing.",
                        "https://upload.wikimedia.org/wikipedia/en/5/55/Following_film_poster.jpg",
                        "https://youtu.be/5q8bBAKNSA8",
                        "(1998)",
                        "69 min.",
                        "Mystery | Thriller")

memento = media.Movie("Memento",
                     "A man creates a strange system to help him remember things; so he can hunt for the murderer of his wife without his short-term memory loss being an obstacle.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                     "https://youtu.be/UFuFFdK7i44",
                     "(2000)",
                     "113 min.",
                     "Mystery | Thriller")

the_prestige = media.Movie("The Prestige",
                     "Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.",
                     "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                     "https://youtu.be/ijXruSzfGEc",
                     "(2006)",
                     "130 min.",
                     "Drama | Mystery | Thriller")

the_dark_knight = media.Movie("The Dark Knight",
                     "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://youtu.be/_PZpmTj1Q8Q",
                     "(2008)",
                     "152 min.",
                     "Action | Crime | Drama")

inception = media.Movie("Inception",
                     "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                     "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                     "https://youtu.be/zp_YGmAoht0",
                     "(2010)",
                     "148 min.",
                     "Action | Mystery | Sci-Fi")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in\
                            space in an attempt to ensure humanity's survival.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://youtu.be/-0AhpfKFOEM",
                           "(2014)",
                           "169 min.",
                           "Adventure | Drama | Sci-Fi")

movies = [following, memento, the_prestige, the_dark_knight, inception, interstellar]

fresh_tomatoes.open_movies_page(movies)
