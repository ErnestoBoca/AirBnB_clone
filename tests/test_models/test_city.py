#!/usr/bin/python3
"""This module conatains the TestCity class"""
from models.city import City
from unittest import TestCase


class TestCity(TestCase):
    """My TestCity class"""
    def test_attr(self):

        self.assertTrue(hasattr(City, "state_id"))
        self.assertIsInstance(City.state_id, str)
        self.assertEqual(City.state_id, "")

        self.assertTrue(hasattr(City, "name"))
        self.assertIsInstance(City.name, str)
        self.assertEqual(City.name, "")
