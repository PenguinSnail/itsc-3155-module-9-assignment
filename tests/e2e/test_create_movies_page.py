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
    }, follow_redirects = True)

    assert response.request.path == "/movies"
    assert response.status_code == 200

def test_invalid_movie_creation(test_app):

    # test to check that the form reloads with an error on the page
    # if the movie title was left blank
    test1 = test_app.post('/movies', data = {
        "movie_title": "",
        "movie_director": "Director",
        "movie_rating": "2"
    }, follow_redirects = True)

    assert test1.request.path == "/movies"
    test_1_data = test1.data.decode('utf-8')
    assert "Error" in test_1_data 

    # test to check that the form reloads with an error on the page
    # if the movie director was left blank
    test2 = test_app.post('/movies', data = {
        "movie_title": "Title",
        "movie_director": "",
        "movie_rating": "5"
    }, follow_redirects = True)

    assert test2.request.path == "/movies"
    test_2_data = test2.data.decode('utf-8')
    assert "Error" in test_2_data 
    
    # test to check that the form reloads with an error on the page
    # if the movie rating was left blank
    test3 = test_app.post('/movies', data = {
        "movie_title": "Title",
        "movie_director": "Director",
        "movie_rating": ""
    }, follow_redirects = True)

    assert test3.request.path == "/movies"
    test_3_data = test3.data.decode('utf-8')
    assert "Error" in test_3_data 