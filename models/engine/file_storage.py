#!/usr/bin/python3
"""
serializes/deserializes Json
"""
import json
import sys


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
    _file_path: Path to JSON file
    _objects: Dictionary storing all objects
    """
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """
        Returns the dictionary _objects
        """
        return self._objects


    def new(self, obj):
        """
        sets in _objects the obj with key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + getattr(obj, "id")
        self._objects[key] = obj

    def save(self):
        """
        serializes _objects to the JSON file
        """
        try:
            with open(FileStorage._file_path, mode='r', encoding='UTF-8') as f:
                r = f.read()
                my_obj = json.loads(r)
        except:
            with open(self._file_path, mode='w', encoding='UTF-8') as f:
                f.write('')
                my_obj = {}
        with open(self._file_path, mode='w', encoding='UTF-8') as f:
            for k, v in FileStorage._objects.items():
                my_obj[k] = v.to_dict()
            my_str = json.dumps(my_obj)
            f.write(my_str)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage._file_path, mode='r') as f:
                from models.base_model import BaseModel
                r = json.load(f)
                for v in r.values():
                    my_obj = BaseModel(**v)
                    self.new(my_obj)
        except:
            pass
