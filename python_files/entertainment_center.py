import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A boy's toy's come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine goes to an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

wolf_of_wall_street = media.Movie("Wolf of Wall Street",
                                  "Rags to riches on wallstreet",
                                  "http://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                  "https://www.youtube.com/watch?v=iszwuX1AK6A")

the_imitation_game = media.Movie("The Imitation Game",
                                 "An artists impression of Alan Turing's life",
                                 "http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")

interstellar = media.Movie("Interstellar",
                           "The search for a new planet to accommodate humanatiy",
                           "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=ePbKGoIGAXY")

inglorious_bastards = media.Movie("Inglorious Bastards",
                                  "Dark comady / drama about WWII",
                                  "http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                  "www.youtube.com/watch?v=prj3URvxcHU")

movies = [toy_story, avatar, wolf_of_wall_street, the_imitation_game, interstellar, inglorious_bastards]

#print media.Movie.VALID_RATINGS
fresh_tomatoes.open_movies_page(movies)
