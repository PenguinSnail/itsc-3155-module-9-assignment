# TODO: Feature 2
# Franky Yang

from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
# test the movie_repository class, specficially the create_movie method
    # creates the repository
    test_repo = get_movie_repository()

    # the size of the list after initial creation
    initial = len(test_repo._db)

    # creates the movie object in the repository
    test_repo.create_movie("Title","Director",5)

    # test to make sure the movie is added
    assert len(test_repo._db) == initial+1

