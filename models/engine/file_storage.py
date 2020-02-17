#!/usr/bin/python3
"""
serializes/deserializes JSON
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

    def del_key(self, key):
        """
        delete a key from _objects
        """
        del self._objects[key]

    def update_obj(self, id, key, value):
        """
        updates/add an object in _objects.
        """
        string = value
        if string.startswith('"') or string.startswith("'"):
            string = string[1:]
        if string.endswith('"') or string.endswith("'"):
            string = string[:-1]
        setattr(self._objects[id], str(key), str(string))

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
        with open(self._file_path, mode='w', encoding='UTF-8') as f:
            my_obj = {}
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
                from models.amenity import Amenity
                from models.base_model import BaseModel
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User
                r = json.load(f)
                for k, v in r.items():
                    cls_name = k.split('.')[0]
                    my_obj = eval(cls_name)(**v)
                    self.new(my_obj)
        except:
            pass
