#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
from models.base_model import BaseModel
import datetime
import unittest
import uuid
import io
import sys

class test_file(unittest.TestCase):
    """
    Test BaseModel class.
    """

    def test_bm(self):
        """
        Test BaseModel class id values.
        """
        bs1 = BaseModel()
        bs2 = BaseModel()
        self.assertTrue(isinstance(bs1, BaseModel))
        self.assertNotEqual(bs1.id, bs2.id)
        bs1.name = "Holberton"
        self.assertEqual(bs1.name, "Holberton")
        self.assertTrue(isinstance(bs1.name, str))
        bs1.age = 5
        self.assertEqual(bs1.age, 5)
        self.assertTrue(isinstance(bs1.age, int))
        self.assertTrue(isinstance(bs1.created_at, datetime.datetime))
        self.assertTrue(isinstance(bs1.updated_at, datetime.datetime))
        self.assertTrue(isinstance(bs1.id, str))
        self.assertTrue(isinstance(bs1.to_dict(), dict))
        self.assertTrue(hasattr(bs1, 'id'))
        self.assertTrue(hasattr(bs1, 'created_at'))
        self.assertTrue(hasattr(bs1, 'updated_at'))
        self.assertTrue(hasattr(bs1, 'age'))
        self.assertTrue(hasattr(bs1, 'name'))
        
        self.assertTrue(hasattr(bs1, '__str__'))
