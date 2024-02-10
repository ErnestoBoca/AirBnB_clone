#!/usr/bin/python3
"""This module contains tests for the FileStorage clss"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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

        storage.new(bm)

        self.assertIn("BaseModel." + bm.id, storage.all().keys())
        self.assertIn(bm, storage.all().values())

        with self.assertRaises(TypeError):
            storage.new()
        with self.assertRaises(TypeError):
            storage.new(None, "")

    def test_save(self):
        bm = BaseModel()
        storage = FileStorage()
        storage.save()

        with open("file.json", "r", encoding="utf-8") as file:
            text_saved = file.read()
            self.assertIn("BaseModel." + bm.id, text_saved)

            with self.assertRaises(TypeError):
                storage.save(None)

    def test_reload(self):
        storage = FileStorage()
        bm = BaseModel()

        storage.save()
        storage.reload()

        self.assertIn("BaseModel." + bm.id, storage.all().keys())

        with self.assertRaises(TypeError):
            storage.reload(None)
