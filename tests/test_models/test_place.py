#!/usr/bin/python3
"""This module contains TestPlace class"""
from models.place import Place
from unittest import TestCase


class TestPlace(TestCase):
    """My TestPlace Module"""
    def test_attr(self):
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertIsInstance(Place.city_id, str)
        self.assertEqual(Place.city_id, "")

        self.assertTrue(hasattr(Place, "user_id"))
        self.assertIsInstance(Place.user_id, str)
        self.assertEqual(Place.user_id, "")

        self.assertTrue(hasattr(Place, "name"))
        self.assertIsInstance(Place.name, str)
        self.assertEqual(Place.name, "")

        self.assertTrue(hasattr(Place, "description"))
        self.assertIsInstance(Place.description, str)
        self.assertEqual(Place.description, "")

        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertIsInstance(Place.number_rooms, int)
        self.assertEqual(Place.number_rooms, 0)

        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertEqual(Place.number_bathrooms, 0)

        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertIsInstance(Place.max_guest, int)
        self.assertEqual(Place.max_guest, 0)

        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertIsInstance(Place.price_by_night, int)
        self.assertEqual(Place.price_by_night, 0)

        self.assertTrue(hasattr(Place, "latitude"))
        self.assertIsInstance(Place.latitude, float)
        self.assertEqual(Place.latitude, 0.0)

        self.assertTrue(hasattr(Place, "longitude"))
        self.assertIsInstance(Place.longitude, float)
        self.assertEqual(Place.longitude, 0.0)

        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertIsInstance(Place.amenity_ids, list)
        self.assertEqual(Place.amenity_ids, [])
