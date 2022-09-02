from app.dao.model.director import SchemaDirector


from flask_restx import Resource, Namespace

from container import director_service

schema_director = SchemaDirector()
schema_directors = SchemaDirector(many=True)
director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorView(Resource):
    def get(self):
        directors = director_service.get_all()
        return schema_directors.dump(directors), 200


@director_ns.route("/<int:d_id>")
class DirectorsView(Resource):
    def get(self, d_id):
        director = director_service.get_one(d_id)
        return schema_director.dump(director), 200
