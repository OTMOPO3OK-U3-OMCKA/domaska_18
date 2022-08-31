from views_movie.dao.model.genre import SchemaGenre


from flask_restx import Resource, Namespace

from container import genre_service

schema_genre = SchemaGenre()
schema_genres = SchemaGenre(many=True)
genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return schema_genres.dump(genres), 200

@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return schema_genre.dump(genre), 200