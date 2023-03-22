# TODO: Feature 4

# Feature 4
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_view_movie_page():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    new_movie = movie_repository.create_movie("Master of Disguise", "Michael Bay", 5)

    test_page = app.test_client()
    response = test_page.get(f'/movies/{new_movie.movie_id}')
    data = response.data.decode('utf-8')
    assert response.status_code == 200

    assert '<p>Michael Bay</p>' in data

    assert '<p>5/5</p>' in data

    assert '<h1 class="mb-5">Information for <em>Master of Disguise</em></h1>' in data