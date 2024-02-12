#!/usr/bin/bash
"""This module contains the TestAmenity class"""
from models.amenity import Amenity
from unittest import TestCase


class TestAmenity(TestCase):
    """My TestAmenity class"""
    def test_attr(self):
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertIsInstance(Amenity.name, str)
        self.assertEqual(Amenity.name, "")
