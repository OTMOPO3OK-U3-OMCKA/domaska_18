from views_movie.dao.director import DirectorDAO
from views_movie.dao.genre import GenreDAO
from views_movie.dao.movie import MovieDAO
from setup_db import db
from views_movie.services.director import DirectorService
from views_movie.services.genre import GenreService
from views_movie.services.movie import MovieService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)