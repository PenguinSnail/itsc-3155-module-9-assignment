# TODO: Feature 6
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_delete(test_app: FlaskClient):
    movie_repository.clear_db()
    
    new_movie1 = movie_repository.create_movie('bonanza', 'frank Sinatra', 4)
    new_movie2 = movie_repository.create_movie('name', 'direct', 2)
    assert len(movie_repository._db) == 2
    
    response = test_app.post(f'/movies/{new_movie1.movie_id}/delete', follow_redirects = True)
    assert len(movie_repository._db) == 1
    assert response.status_code == 200