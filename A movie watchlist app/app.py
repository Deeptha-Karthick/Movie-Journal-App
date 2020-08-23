import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app
7) Search for a movie
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie Name: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")  # date and format of the date we are gonna parse
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"------{heading} Movies-----")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(
            release_date)  # getting the timestamp value and changing it into timestamp object
        human_date = movie_date.strftime("%b %d %Y")  # changing the timestamp object into string format
        print(f"{_id}: {title} on {human_date}")
    print("----\n")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID ")
    database.watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def prompt_search_movies():
    search_term = input("Enter the partial movie title")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print("Found no movies for the search")


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)  # True is for upcoming movies
        print_movie_list("upcoming movies", movies)
    elif user_input == "3":
        movies = database.get_movies()  # True is for upcoming movies
        print_movie_list("all movies", movies)
    elif user_input == "4":
        prompt_watch_movie()

    elif user_input == "5":
        username = input("Username: ")
        movies = database.get_watched_movies(username)  # True is for upcoming movies
        if movies:
            print_movie_list("watched", movies)
        else:
            print("No movies to display")

    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")
