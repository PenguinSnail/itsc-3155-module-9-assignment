# TODO: Feature 3
# Tyler Jordan

from src.repositories.movie_repository import get_movie_repository

#Test to make sure the input is a title
def test_input_string(test_app):
    test_repo = get_movie_repository()
    test_repo.clear_db()

    movie = test_repo.create_movie("test","director",2)
    id = movie.movie_id 

    response = test_app.get('/movies/search', query_string={
        'title': 'test'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == ("/movies/"+str(id))

#Redirecting to same page when not in repository
def test_input_string_error(test_app):
    response = test_app.get('/movies/search', query_string={
        'title': 'asdfhj;o' 
    }, follow_redirects=True)
    assert response.request.path == "/movies/search"

    data = response.data.decode('utf-8')
    assert '<p>Error: Movie not Found</p>' in data

#Testing if page renders
def test_search_page(test_app):
    response = test_app.get('/movies/search', follow_redirects=True)
    data = response.data.decode('utf-8')
    assert '<h1 class="mb-5">Search Movie Ratings</h1>' in data

    



