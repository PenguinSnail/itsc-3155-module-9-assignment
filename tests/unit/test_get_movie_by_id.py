# Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    new_movie = movie_repository.create_movie("Master of Disguise", "Michael Bay", 5)
    movie_id = new_movie.movie_id
    tested_movie = movie_repository.get_movie_by_id(movie_id)
    assert tested_movie == new_movie

def test_get_movie_wrong_id():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    try: # we want it to error
       movie_repository.get_movie_by_id(4)
       assert False
    except:
        assert True

