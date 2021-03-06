import media
import fresh_tomatoes

# Manually added movie data

shawshank_remdemption = media.Movie(
        "The Shawshank Redemption",
        "Framed for murder, a man gains admiration in prison for his sense{0}"
        " of hope",
        "http://image.tmdb.org/t/p/w342/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
        "https://www.youtube.com/watch?v=6hB3S9bIaco",
        1994,
        "Tim Robbins, Morgan Freeman, Bob Gunton")
godfather = media.Movie(
        "The Godfather",
        "The aging patriarch of organized crime dynasty transfer control of{0}"
        " his empire to reluctant son",
        "http://image.tmdb.org/t/p/w342/d4KNaTrltq6bpkFS01pYtyXa09m.jpg",
        "https://www.youtube.com/watch?v=w0VGcWHkNeA",
        1972,
        "Marlon Brando, Al Pacino, James Caan")
cuckoos_nest = media.Movie(
        "One Flew Over the Cuckoos Nest",
        "mental patient inspires his fellow patients to rebel against the{0}"
        " authoritarian rule",
        "http://image.tmdb.org/t/p/w342/srr59GKJdDXPwnWlew9NoYfOvYV.jpg",
        "https://www.youtube.com/watch?v=2WSyJgydTsA",
        1975,
        "Jack Nicholson, Louise Fletcher, Michael Berryman")
empire_strikes_back = media.Movie(
        "Star Wars: Episode V - The Empire Strikes Back",
        "Luke Skywalker learns the ways of the Jedi from master Yoda to{0}"
        " fight the evil empire",
        "http://image.tmdb.org/t/p/w342/6u1fYtxG5eqjhtCPDx04pJphQRW.jpg",
        "https://www.youtube.com/watch?v=96v4XraJEPI",
        1980,
        "Mark Hamill, Harrison Ford, Carrie Fisher ")
matrix = media.Movie(
        "The Matrix",
        "hacker learns the truth about his reality and his role in the war{0}"
        " against its controllers",
        "http://image.tmdb.org/t/p/w342/ZPMhHXEhYB33YoTZZNNmezth0V.jpg",
        "https://www.youtube.com/watch?v=Q8g9zL-JL8E",
        1999,
        "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")
spirited_away = media.Movie(
        "Spirited Away",
        "a young girl wanders away from her parents to a world with strange{0}"
        " monster-like animals",
        "http://image.tmdb.org/t/p/w342/dL11DBPcRhWWnJcFXl9A07MrqTI.jpg",
        "https://www.youtube.com/watch?v=6az9wGfeSgM",
        2001,
        "Daveigh Chase, Suzanne Pleshette, Miyu Irino")

# Store movies in an array to pass to outside function
movies = [spirited_away, matrix, shawshank_remdemption, godfather,
          empire_strikes_back, cuckoos_nest]

# Call external rendering function with movie data
fresh_tomatoes.open_movies_page(movies)
