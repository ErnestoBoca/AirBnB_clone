#!/usr/bin/python3
"""This module conatinas the FileStorage class"""
import json


class FileStorage:
    """ This class serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        json_string = json.dumps(obj_dict)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json_file.write(json_string)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        classes = {
            "BaseModel": BaseModel
        }
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_file:
                obj_dict = json.loads(json_file.read())
                for value in obj_dict.values():
                    new_obj = classes[value["__class__"]](**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass
