import unittest

from src.lab4.recomendation import *


class TestFilm(unittest.TestCase):
    def test_init(self):
        film = Film("The Matrix")
        self.assertEqual(film.title, "The Matrix")


class TestUser(unittest.TestCase):
    def test_init(self):
        user_films = [1, 2, 3]
        user = User(user_films)
        self.assertEqual(user.films, user_films)


class TestUserDB(unittest.TestCase):
    def setUp(self):
        self.user_db = User_DB([User([2, 1, 3]), User([1, 4, 3]), User([2, 2, 2, 2, 2, 3])])
        self.users = self.user_db.get_all()

    def test_load_users(self):
        self.assertIsInstance(self.users, list)
        self.assertEqual(len(self.users), 3)  # Assuming there are 3 users in the test file


class TestFilmDB(unittest.TestCase):
    def setUp(self):
        self.film_db = Film_DB({1: Film("Мстители: Финал"), 2: Film("Хатико"), 3: Film("Дюна"), 4: Film("Унесённые призраками")})
        self.films = self.film_db.get_all()

    def test_load_films(self):
        self.assertIsInstance(self.films, dict)
        self.assertEqual(len(self.films), 4)  # Assuming there are 4 films in the test file


class TestRecommendFilm(unittest.TestCase):
    def setUp(self):
        self.film_db = Film_DB({1: Film("Мстители: Финал"), 2: Film("Хатико"), 3: Film("Дюна"), 4: Film("Унесённые призраками")})
        self.films = self.film_db.get_all()

        self.user_db = User_DB([User([2, 1, 3]), User([1, 4, 3]), User([2, 2, 2, 2, 2, 3])])
        self.users = self.user_db.get_all()

        self.current_user = User([2, 4])

    def test_recommend_film(self):
        recommended_film = recommend_film(self.films, self.users, self.current_user)
        self.assertIn(recommended_film, ["Дюна"])


if __name__ == "__main__":
    unittest.main()
