# TODO: Feature 6
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_delete_movie():
    movie_repository.clear_db()

    new_movie = movie_repository.create_movie('bonanza', 'frank Sinatra', 4)

    # Checking that the movie was added to the repository
    assert len(movie_repository._db) == 1
    movie_repository.delete_movie(new_movie.movie_id)
    # Checking that the movie was deleted from the repository
    assert len(movie_repository._db) == 0
    