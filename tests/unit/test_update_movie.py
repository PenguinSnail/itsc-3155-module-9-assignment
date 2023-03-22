from src.repositories.movie_repository import get_movie_repository

movie_repo = get_movie_repository()

def test_update_movie():
    movie_repo.clear_db()
    new_movie = movie_repo.create_movie('My Movie', 'The Director', 5)

    assert movie_repo.get_movie_by_id(new_movie.movie_id).rating == 5

    movie_repo.update_movie(new_movie.movie_id, 'My Movie', 'The Director', 1)

    assert movie_repo.get_movie_by_id(new_movie.movie_id).rating == 1
