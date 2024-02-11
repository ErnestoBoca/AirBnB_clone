#!/usr/bin/python3
"""This module conatins the TestBaseModel class"""
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(TestCase):
    """This class contains the test cases for the BaseModel class"""
    def test_init(self):
        """Tests the __init__ method"""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertIsInstance(model1, BaseModel)

        self.assertTrue(hasattr(model1, "id"))
        self.assertTrue(hasattr(model1, "created_at"))
        self.assertTrue(hasattr(model1, "updated_at"))

        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)

        self.assertNotEqual(model1.id, model2.id)
        self.assertLess(model1.created_at, model2.created_at)
        self.assertLess(model1.updated_at, model2.updated_at)

        self.assertIn(BaseModel(), storage.all().values())

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_int_kwargs(self):
        """Tests the init method with arguments"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_str(self):
        """Tests the __str__ function"""
        model1 = BaseModel()
        goal = "[{}] ({}) {}".format(
            model1.__class__.__name__, model1.id, model1.__dict__
        )
        self.assertEqual(model1.__str__(), goal)

    def test_save(self):
        """Tests the save method"""
        model = BaseModel()
        date1 = model.updated_at
        model.save()
        date2 = model.updated_at

        self.assertNotEqual(date1, date2)
        self.assertLess(date1, date2)

        model_id = "BaseModel." + model.id
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

        with self.assertRaises(TypeError):
            model.save(None)

    def test_to_dict(self):
        """Tests the to_dict method"""
        model = BaseModel()
        BaseModel.count = 10
        model.name = "My first model"
        model_dict = model.to_dict()

        self.assertNotEqual(model.to_dict(), model.__dict__)
        self.assertIsInstance(model_dict, dict)

        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertNotIn("count", model_dict)

        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

        date_format_regex = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}'
        self.assertRegex(model_dict["created_at"], date_format_regex)
        self.assertRegex(model_dict["updated_at"], date_format_regex)

        with self.assertRaises(TypeError):
            model.to_dict(None)

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)
