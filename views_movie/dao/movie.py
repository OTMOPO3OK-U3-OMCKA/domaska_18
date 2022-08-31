from views_movie.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_director_id(self, requested):
        return self.session.query(Movie).filter(Movie.director_id == requested)

    def get_genre_id(self, requested):
        return self.session.query(Movie).filter(Movie.genre_id == requested)

    def get_year(self, requested):
        return self.session.query(Movie).filter(Movie.year == requested)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data, mid):
        movie = self.get_one(mid)
        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()