#!/usr/bin/python3
"""
FileStorage class Unittest cases.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class testFileStorage(unittest.TestCase):
    """
    FileStorage class test cases.
    """

    def test_fs(self):
        """
        verify fs
        """
        st = FileStorage()
        objs = storage.all()
        for k, v in objs.items():
            self.assertTrue(issubclass(eval(k.split('.')[0]), baseModel))
