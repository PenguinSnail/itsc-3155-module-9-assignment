from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

movie_repo = get_movie_repository()

def test_edit_page(test_app: FlaskClient):
    movie_repo.clear_db()
    new_movie = movie_repo.create_movie('My Movie', 'The Director', 5)
    response = test_app.get(f'/movies/{new_movie.movie_id}/edit')
    response_data = response.data.decode('utf-8')

    assert '<h1 class="mb-5">Edit Movie Rating</h1>' in response_data
    assert '<input type="text" name="movie_title" class="form-control" placeholder="Enter the movie name" value="My Movie" required>' in response_data
    assert '<input type="text" name="movie_director" class="form-control" placeholder="Enter the movie director" value="The Director" required>' in response_data
    assert '<input type="number" name="movie_rating" min="1" max="5" class="form-control" placeholder="Rate the movie" value="5" required>' in response_data

def test_edit_submit(test_app: FlaskClient):
    movie_repo.clear_db()
    new_movie = movie_repo.create_movie('My Movie', 'The Director', 5)
    response = test_app.post(f'/movies/{new_movie.movie_id}', data = {
        "movie_title": 'My Movie',
        "movie_director": 'The Director',
        "movie_rating": 1
    }, follow_redirects = True)

    assert response.status_code == 200
    assert movie_repo.get_movie_by_id(new_movie.movie_id).rating == 1

def test_update_validation(test_app: FlaskClient):
    movie_repo.clear_db()
    new_movie = movie_repo.create_movie('My Movie', 'The Director', 5)

    # no title
    response = test_app.post(f'/movies/{new_movie.movie_id}', data = {
        "movie_title": '',
        "movie_director": 'The Director',
        "movie_rating": 5
    }, follow_redirects = True)
    assert "Error: Invalid form data" in response.data.decode('utf-8'), "Should error when no title is given"

    # no director
    response = test_app.post(f'/movies/{new_movie.movie_id}', data = {
        "movie_title": 'The Movie',
        "movie_director": '',
        "movie_rating": 5
    }, follow_redirects = True)
    assert "Error: Invalid form data" in response.data.decode('utf-8'), "Should error when no director is given"

    # no rating
    response = test_app.post(f'/movies/{new_movie.movie_id}', data = {
        "movie_title": 'The Movie',
        "movie_director": 'The Director',
        "movie_rating": ''
    }, follow_redirects = True)
    assert "Error: Invalid form data" in response.data.decode('utf-8'), "Should error when no rating is given"

    # non-integer rating
    response = test_app.post(f'/movies/{new_movie.movie_id}', data = {
        "movie_title": 'The Movie',
        "movie_director": 'The Director',
        "movie_rating": 'bad rating'
    }, follow_redirects = True)
    assert "Error: Invalid form data" in response.data.decode('utf-8'), "Should error when rating is not a number"

    # rating below bounds
    response = test_app.post(f'/movies/{new_movie.movie_id}', data = {
        "movie_title": 'The Movie',
        "movie_director": 'The Director',
        "movie_rating": 0
    }, follow_redirects = True)
    assert "Error: Invalid form data" in response.data.decode('utf-8'), "Should error when rating is out of bounds"

    # rating above bounds
    response = test_app.post(f'/movies/{new_movie.movie_id}', data = {
        "movie_title": 'The Movie',
        "movie_director": 'The Director',
        "movie_rating": 6
    }, follow_redirects = True)
    assert "Error: Invalid form data" in response.data.decode('utf-8'), "Should error when rating is out of bounds"
