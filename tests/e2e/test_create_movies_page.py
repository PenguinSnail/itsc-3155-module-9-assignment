# TODO: Feature 2
# Franky Yang

from app import app

def create_movie(test_app,Title,Director,Rating):
    response = test_app.post('/movies', data = {
        "movie_title": Title,
        "movie_director": Director,
        "movie_rating": Rating
    }, follow_redirects = True)
     
    return response

# test to ensure that the page still loads properly after creating a movie 
def test_valid_movie_creation(test_app):
    test_valid_movie_creation = create_movie(test_app,"Title","Director","5")
    assert test_valid_movie_creation.request.path == "/movies"
    assert test_valid_movie_creation.status_code == 200


def test_no_title(test_app):
# test to check that the form reloads with an error on the page
# # if the movie title was left blank
    test_no_title = create_movie(test_app,"","Director","5")
    assert test_no_title.request.path == "/movies"
    assert "Error" in test_no_title.data.decode('utf-8')


def test_no_director(test_app):
# test to check that the form reloads with an error on the page
# if the movie director was left blank
    test_no_director = create_movie(test_app,"Title","","5")
    assert test_no_director.request.path == "/movies"
    assert "Error" in test_no_director.data.decode('utf-8')

 
def test_no_rating(test_app):
# test to check that the form reloads with an error on the page
# if the movie rating was left blank   
    test_no_rating = create_movie(test_app,"Title","Director","")
    assert test_no_rating.request.path == "/movies"
    assert "Error" in test_no_rating.data.decode('utf-8')


def test_rating_outOfBounds(test_app):
# test to check that the form reloads with an error on the page
# if the movie rating was out of bounds
    test_rating_larger = create_movie(test_app,"Title","Director","12")
    assert test_rating_larger.request.path == "/movies"
    assert "Error" in test_rating_larger.data.decode('utf-8')

    test_rating_smaller = create_movie(test_app,"Title","Director","-12")
    assert test_rating_smaller.request.path == "/movies"
    assert "Error" in test_rating_smaller.data.decode('utf-8')


def test_rating_nonNumber(test_app):
# test to check that the form reloads with an error on the page
# if the movie rating was not a number
    test_rating_outOfBounds = create_movie(test_app,"Title","Director","asd")
    assert test_rating_outOfBounds.request.path == "/movies"
    assert "Error" in test_rating_outOfBounds.data.decode('utf-8')


def test_rating_notInt(test_app):
# test to check that the form reloads with an error on the page
# if the movie rating was not a integer
    test_rating_outOfBounds = create_movie(test_app,"Title","Director","asd")
    assert test_rating_outOfBounds.request.path == "/movies"
    assert "Error" in test_rating_outOfBounds.data.decode('utf-8')