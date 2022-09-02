# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
# from flask_restx import Resource, Namespace
#
# book_ns = Namespace('books')
#
#
# @book_ns.route('/')
# class BooksView(Resource):
#     def get(self):
#         return "", 200
#
#     def post(self):
#         return "", 201
from flask_restx import Resource, Namespace

from container import movie_service
from app.dao.model.movie import SchemaMovie


from flask import request
movie_ns = Namespace('movies')
add_ns = Namespace("add_in_DB")

schema_movie = SchemaMovie()
schema_movies = SchemaMovie(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        try:
            director_id = request.args.get("director_id")
            genre_id = request.args.get("genre_id")
            year = request.args.get("year")
            if director_id != None and genre_id == None and year == None:
                movies_director = movie_service.get_director_id(director_id)
                return schema_movies.dump(movies_director), 200
            elif genre_id != None and director_id == None and year == None:
                movies_genre = movie_service.get_genre_id(genre_id)
                return schema_movies.dump(movies_genre), 200
            elif genre_id == None and director_id == None and year != None:
                movies_year = movie_service.get_year(year)
                return schema_movies.dump(movies_year), 200
            else:
                return schema_movies.dump(movie_service.get_all()), 200
        except:
            return "", 200
    def post(self):
        try:
            movie = request.json
            return schema_movie.dump(movie_service.create(movie)), 201
        except:
            return '', 201

@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return schema_movie.dump(movie), 200


    def put(self, mid):
        my_movie = request.json
        movie = movie_service.update(my_movie, mid)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204

@add_ns.route("/")
class Add_in_DBView(Resource):
    def get(self):
        movie_service.add_in_DB()
        return "", 200