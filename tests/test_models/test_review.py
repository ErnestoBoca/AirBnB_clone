#!/usr/bin/python3
"""This module contains the TestReview class"""
from models.review import Review
from unittest import TestCase


class TestReview(TestCase):
    """My TestReview class"""

    def test_attr(self):

        self.assertTrue(hasattr(Review, "place_id"))
        self.assertIsInstance(Review.place_id, str)
        self.assertEqual(Review.place_id, "")

        self.assertTrue(hasattr(Review, "user_id"))
        self.assertIsInstance(Review.user_id, str)
        self.assertEqual(Review.user_id, "")

        self.assertTrue(hasattr(Review, "text"))
        self.assertIsInstance(Review.text, str)
        self.assertEqual(Review.text, "")
