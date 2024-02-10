#!/usr/bin/python3
"""This module contains tests for the User class"""
from models.user import User
from unittest import TestCase


class TestUser(TestCase):
    """test cases for the User class"""

    def test_init(self):
        user = User()

        self.assertTrue(hasattr(user, "email"))
        self.assertIsInstance(user.email, str)
        self.assertEqual(user.email, "")

        self.assertTrue(hasattr(user, "password"))
        self.assertIsInstance(user.password, str)
        self.assertEqual(user.password, "")

        self.assertTrue(hasattr(user, "first_name"))
        self.assertIsInstance(user.first_name, str)
        self.assertEqual(user.first_name, "")

        self.assertTrue(hasattr(user, "last_name"))
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.last_name, "")
