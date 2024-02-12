#!/usr/bin/python3
"""This module contains tests for the FileStorage clss"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Tests the methods of FileStorage"""

    def test_attrs(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(type(models.storage), FileStorage)

        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all(self):
        storage = FileStorage()
        obj_dict = storage.all()

        self.assertIsInstance(obj_dict, dict)
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        storage = FileStorage()
        bm = BaseModel()
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        storage.new(bm)
        storage.new(user)
        storage.new(state)
        storage.new(city)
        storage.new(amenity)
        storage.new(place)
        storage.new(review)

        self.assertIn("BaseModel." + bm.id, storage.all().keys())
        self.assertIn(bm, storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

        with self.assertRaises(TypeError):
            storage.new(None)
        with self.assertRaises(TypeError):
            storage.new(3, "")

    def test_save(self):
        bm = BaseModel()
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()
        storage = FileStorage()

        storage.new(bm)
        storage.new(user)
        storage.new(state)
        storage.new(city)
        storage.new(amenity)
        storage.new(place)
        storage.new(review)

        storage.save()

        with open("file.json", "r", encoding="utf-8") as file:
            text_saved = file.read()
            self.assertIn("BaseModel." + bm.id, text_saved)
            self.assertIn("User." + user.id, text_saved)
            self.assertIn("State." + state.id, text_saved)
            self.assertIn("City." + city.id, text_saved)
            self.assertIn("Amenity." + amenity.id, text_saved)
            self.assertIn("Place." + place.id, text_saved)
            self.assertIn("Review." + review.id, text_saved)

            with self.assertRaises(TypeError):
                storage.save(None)

    def test_reload(self):
        storage = FileStorage()
        bm = BaseModel()
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        storage.new(bm)
        storage.new(user)
        storage.new(state)
        storage.new(city)
        storage.new(amenity)
        storage.new(place)
        storage.new(review)

        storage.save()
        storage.reload()

        self.assertIn("BaseModel." + bm.id, storage.all().keys())
        self.assertIn("User." + user.id, storage.all().keys())
        self.assertIn("State." + state.id, storage.all().keys())
        self.assertIn("City." + city.id, storage.all().keys())
        self.assertIn("Amenity." + amenity.id, storage.all().keys())
        self.assertIn("Place." + place.id, storage.all().keys())
        self.assertIn("Review." + review.id, storage.all().keys())

        with self.assertRaises(TypeError):
            storage.reload(None)
