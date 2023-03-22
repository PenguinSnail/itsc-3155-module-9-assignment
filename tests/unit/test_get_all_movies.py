# TODO: Feature 1

from src.repositories.movie_repository import get_movie_repository
def test_get_all_movies():
     
     movie_repository = get_movie_repository()
     movie_repository.clear_db()
     movie_repository.create_movie('test move', 'test director', 5)
     test = len(movie_repository.get_all_movies())
     assert test ==0

     movie_repository.create_movie('test move', 'test director', 5)
     test = len(movie_repository.get_all_movies())
     assert test ==1

     movie_repository.create_movie('test move2', 'test director2', 5)
     test = len(movie_repository.get_all_movies())
     assert test ==2
     
     movie_repository.clear_db()
     test = len(movie_repository.get_all_movies())
     assert test ==0
