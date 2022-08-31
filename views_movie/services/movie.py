from views_movie.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_director_id(self, requested):
        return self.dao.get_director_id(requested)

    def get_genre_id(self, requested):
        return self.dao.get_genre_id(requested)

    def get_year(self, requested):
        return self.dao.get_year(requested)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, mid):
        return self.dao.update(data, mid)

    def delete(self, mid):
        return self.dao.delete(mid)
