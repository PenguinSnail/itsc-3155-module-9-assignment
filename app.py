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

    return render_template('list_all_movies.html', list_movies_active=True, moviedict = movie_repository.get_all_movies())


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
    
    # tries to convert rating into a number if not rejects form
    try:
        rating = int(request.form.get("movie_rating"))

    except ValueError:
        return redirect('/movies/new',create_rating_active=True,error= True)

    # checks all inputs to make sure none of them are blank
    if not title or not director:
        return redirect('/movies/new',create_rating_active=True,error= True)
 
    # checks if rating is within boundaries
    if rating > 5 or rating < 1:
        return redirect('/movies/new',create_rating_active=True,error= True)

    # then creates a movie
    new_movie = movie_repository.create_movie(title,director,rating)
    print(new_movie.movie_id)
#    print(title)
#    print(director)
#    print(rating)

    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    #feature 4: get movie info and send to HTML
    movie = movie_repository.get_movie_by_id(movie_id)
    title = movie.title
    director = movie.director
    rating = movie.rating

    return render_template('get_single_movie.html', movie_director=director, movie_title=title, movie_rating=rating, movie_id=movie_id)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id=movie_id)
    if movie:
        return render_template('edit_movies_form.html', id=movie_id, title=movie.title, director=movie.director, rating=movie.rating)
    return redirect('/movies')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    title = request.form.get("movie_title").strip()
    director = request.form.get("movie_director").strip()
    rating = request.form.get("movie_rating", type=int)

    # check all fields exist and rating is between 1 and 5
    if not title or not director or not rating or rating > 5 or rating < 1:
        movie = movie_repository.get_movie_by_id(movie_id=movie_id)
        if movie:
            return render_template('edit_movies_form.html', id=movie_id, title=movie.title, director=movie.director, rating=movie.rating, error=True)
        return redirect('/movies')

    movie_repository.update_movie(movie_id=movie_id, title=title, director=director, rating=rating)
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
