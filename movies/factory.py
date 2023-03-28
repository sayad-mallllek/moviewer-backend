from faker import Faker, factory
from faker.providers import internet
from .models import Movie, Genre, InitialMovieDump

fake = Faker()
Faker.seed(313)

genres = [
    "Action",
    "Drama",
    "Adventure",
    "Sci-Fi",
    "Comedy",
    "Horror",
    "Documentary",
]

movies = [
    {
        "title": "Need For Speed",
        "year": 2014,
        "genre": "Action",
        "director": "Scott Waugh",
        "plot": "A young man needs to be able to run faster.",
        "runtime": 100,
        "rental_price": 4.49,
    },
    {
        "title": "Halloween",
        "year": 2018,
        "genre": "Horror",
        "director": "Michael Jackson",
        "plot": "A young man needs to be able to run faster.",
        "runtime": 120,
        "rental_price": 6.49,
        "purchase_price": 69.99,
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "plot": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
        "runtime": 169,
        "rental_price": 7.49,
        "purchase_price": 79.99,
    },
]


def create_initial_genres():
    for genre in genres:
        Genre.objects.create(name=genre)


def create_initial_movies():
    for movie in movies:
        Movie.objects.create(
            title=movie.get("title"),
            year=movie.get("year"),
            Genre=Genre.objects.get(name=movie.get("genre")),
            director=movie.get("director"),
            plot=movie.get("plot"),
            runtime=movie.get("runtime"),
            rental_price=movie.get("rental_price"),
            purchase_price=movie.get("purchase_price"),
        )


def confirm_initial_data_dump():
    InitialMovieDump.objects.create(has_been_dumped=True)


def create_initial_data_if_none_exists():
    print("Creating initial Movie data if none exists...")
    if InitialMovieDump.objects.filter(has_been_dumped=True).exists():
        print("Initial Movie data already exists.")
        return
    create_initial_genres()
    create_initial_movies()
    confirm_initial_data_dump()
    print("Initial Movie data has been created.")


if __name__ == "__main__":
    create_initial_data_if_none_exists()
