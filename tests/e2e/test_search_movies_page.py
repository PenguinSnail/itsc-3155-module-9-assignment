# TODO: Feature 3
# Tyler Jordan

import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture(scope = 'module')
def test_app():
    app.test_client()
    return app.test_client()

#Test to make sure the input is a title
def test_input_string(test_app):
    test_repo = get_movie_repository()
    test_repo.create_movie("test","director",2)
    movie = test_repo.get_movie_by_title("test")
    id = movie.movie_id 

    response = test_app.get('/movies/search', data={
        'title': 'test'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == ("/movies/"+str(id))

#Redirecting to same page when not in repository
def test_input_string_error(test_app):
    response = test_app.get('/movies/search', follow_redirects=True)
    assert response.request.path == "/movies/search"


    



