# TODO: Feature 1

from app import app
from src.repositories.movie_repository import get_movie_repository
def test_all_movies_page():
    movie_repository = get_movie_repository()
    movie_repository.create_movie('test movie', 'test director', 5)
    assert len(movie_repository.get_all_movies()) ==1

    test_movie_page = app.test_client()
    response = test_movie_page.get('/movies')
    data = response.data.decode('utf-8')

    assert response.status_code==200
    assert '<td>test movie</td>' in data
    assert '<td>5</td>' in data