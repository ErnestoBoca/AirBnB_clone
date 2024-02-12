#!/usr/bin/python3
"""This module contains the TestState class"""
from models.state import State
from unittest import TestCase


class TestState(TestCase):
    """My TestState class"""
    def test_attr(self):
        self.assertTrue(hasattr(State, "name"))
        self.assertIsInstance(State.name, str)
        self.assertEqual(State.name, "")
