#!/usr/bin/python3
"""This module conatins the TestBaseModel class"""
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime


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

    def test_int_kwargs(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        
        for key, value in my_model_json.items():
            if key != "__class__":
                self.assertTrue(hasattr(my_new_model, key))
                
                if key == "created_at" or key == "updated_at":
                    self.assertIsInstance(getattr(my_new_model, key),
                            datetime)
                    self.assertEqual(datetime.strptime(value,
                        "%Y-%m-%dT%H:%M:%S.%f"), getattr(my_new_model, key))
                else:
                    self.assertEqual(value, getattr(my_new_model, key))

    def test_str(self):
        """Tests the __str__ function"""
        model1 = BaseModel()
        goal = "[{}] ({}) {}".format(model1.__class__.__name__,
                model1.id, model1.__dict__)
        self.assertEqual(model1.__str__(), goal)

    def test_save(self):
        """Tests the save method"""
        model = BaseModel()
        date1 = model.updated_at
        model.save()
        date2 = model.updated_at

        self.assertNotEqual(date1, date2)

    def test_to_dict(self):
        """Tests the to_dict method"""
        model = BaseModel()
        BaseModel.count = 10
        model.name = "My first model"
        model_dict = model.to_dict()

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
        
