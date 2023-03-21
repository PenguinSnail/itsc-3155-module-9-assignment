import pytest
from app import app


# TODO: Feature 2

# Test to see if page adds to the list
@pytest.fixture(scope = 'module')
def test_app():
    return app.test_client()

def test_valid_movie_creation(test_app):

    response = test_app.post('/movies', data = {
        "movie_title": "Title",
        "movie_director": "Director",
        "movie_rating": "3"
    },follow_redirects = True)

    assert response.request.path == "/movies"

def test_invalid_movie_creation(test_app):

    response = test_app.post('/movies', data = {
        "movie_title": "Title",
        "movie_director": "Director",
        "movie_rating": ""
    },follow_redirects = True)

    assert response.request.path == 302