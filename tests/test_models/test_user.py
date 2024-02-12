#!/usr/bin/python3
"""This module contains tests for the User class"""
from models.user import User
from unittest import TestCase


class TestUser(TestCase):
    """test cases for the User class"""

    def test_init(self):
        
        self.assertTrue(hasattr(User, "email"))
        self.assertIsInstance(User.email, str)
        self.assertEqual(User.email, "")

        self.assertTrue(hasattr(User, "password"))
        self.assertIsInstance(User.password, str)
        self.assertEqual(User.password, "")

        self.assertTrue(hasattr(User, "first_name"))
        self.assertIsInstance(User.first_name, str)
        self.assertEqual(User.first_name, "")

        self.assertTrue(hasattr(User, "last_name"))
        self.assertIsInstance(User.last_name, str)
        self.assertEqual(User.last_name, "")
