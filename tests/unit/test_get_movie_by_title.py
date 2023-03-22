# TODO: Feature 3
# Tyler Jordan

from src.repositories.movie_repository import get_movie_repository

def test_find_movie_name():
    test_repo = get_movie_repository()

    test_repo.create_movie("Movie","Director",1)
    test_movie = test_repo.get_movie_by_title("Movie")

    assert test_movie.title == "Movie"

def test_find_no_movie_name():
    test_repo = get_movie_repository()
    assert test_repo.get_movie_by_title("None") == None