from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    
    # puts the form information from the html into variables
    title = request.form.get("movie_title").strip()
    director = request.form.get("movie_director").strip()
    
    # trys to convert rating into a number if not rejects form
    try:
        rating = int(request.form.get("movie_rating"))

    except ValueError:
        return redirect('/movies/new',create_rating_active=True,error= True)
        return render_template('create_movies_form.html', create_rating_active=True,error= True)

    # checks all inputs to make sure none of them are blank
    if not title or not director:
        return redirect('/movies/new',create_rating_active=True,error= True)
        return render_template('create_movies_form.html', create_rating_active=True,error= True)
 
    # checks if rating is within boundries
    if rating > 5 or rating < 1:
        return redirect('/movies/new',create_rating_active=True,error= True)
        return render_template('create_movies_form.html', create_rating_active=True,error= True)

    # then creates a movie
    movie_repository.create_movie(title,director,rating)

    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
