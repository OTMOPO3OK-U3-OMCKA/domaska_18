# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

# from flask import Flask
# from flask_restx import Api
#
# from config import Config
# from models import Review, Book
# from setup_db import db
# from app.books import book_ns
# from app.reviews import review_ns
#
# функция создания основного объекта app
# def create_app(config_object):
#     app = Flask(__name__)
#     app.config.from_object(config_object)
#     register_extensions(app)
#     return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
# def register_extensions(app):
#     db.init_app(app)
#     api = Api(app)
#     api.add_namespace(...)
#     create_data(app, db)
#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)


from flask import Flask
from flask_restx import Api

from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


from setup_db import db
from config import Config
from app.views.movies import movie_ns
from app.views.genres import genre_ns
from app.views.directors import director_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


def create_data():
    #db.drop_all()
    #db.create_all()
    b = Genre(name="супер-флай_жанр")
    c = Director(name="жорик")
    a = Movie(title="полет носка",
              description="3 часа полета, муть страшная",
              trailer="не знаю что в трейлере",
              year=2000,
              rating=10,
              genre=b,
              director=c)
    db.session.add_all([b, c, a])
    db.session.commit()


if __name__ == "__main__":
    config = Config()
    app = create_app(config)
    configure_app(app)
    create_data()
    app.run()

