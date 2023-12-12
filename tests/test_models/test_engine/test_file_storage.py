#!/usr/bin/python3
'''
    testing: model thats contain a FileStorage class that
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    ''' Represent TestFileStorage class '''
    def setUp(self):
        '''
            init classes:
                store from FileStorage
                obj from BaseModel
        '''
        self.store = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        ''' Remove (file.json) after testing '''
        filename = 'file.json'
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

    def test_setup(self):
        ''' Checks if store and obj classes are presents '''
        _store = self.store
        _object = self.obj
        self.assertIsInstance(_store, FileStorage)
        self.assertIsInstance(_object, BaseModel)

    def test_objects_type(self):
        ''' Checks the type of __objects -> should be a dict '''
        _store = self.store
        # you can't access to __objects because it's private attribute
        # thats why, I will use all() method to checks the return value
        self.assertIsInstance(_store.all(), dict)

    def test_all_method(self):
        ''' Test: all() method '''
        _store = self.store
        nw_store = FileStorage()
        self.assertIsInstance(_store.all(), dict)
        self.assertIsInstance(nw_store.all(), dict)
        self.assertEqual(type(_store.all()), type(nw_store.all()))

    def test_new_method(self):
        ''' Test: new() method '''
        _store = self.store
        # create 2 objects from BaseModel for testing
        _object = self.obj
        nw_obj = BaseModel()
        # store objects
        _store.new(_object)
        _store.new(nw_obj)
        # checks the len of __objects dict
        # self.assertEqual(len(_store.all()), 2)
        # checks the key for each obj in __objects
        _object_k = f"{_object.__class__.__name__}.{_object.id}"
        nw_obj_k = f"{nw_obj.__class__.__name__}.{nw_obj.id}"
        self.assertTrue(_object_k in _store.all())
        self.assertTrue(nw_obj_k in _store.all())

    def test_save_method(self):
        ''' Test: save() method '''
        # checks file exists
        filename = "file.json"
        _store = self.store
        _store.save()
        self.assertTrue(os.path.isfile(filename))

    def test_file_reading(self):
        ''' Checks file data '''
        filename = "file.json"
        _object = self.obj
        _store = self.store
        _store.save()
        _store.new(_object)

        with open(filename, 'r') as file:
            data = json.load(file)
        self.assertTrue(type(data) is dict)

    def test_file_data_type(self):
        ''' Checks the data type in file.json '''
        filename = "file.json"
        _object = self.obj
        _store = self.store
        _store.save()
        _store.new(_object)

        with open(filename, 'r') as file:
            data = file.read()
        self.assertIsInstance(data, str)

    def test_reload_method(self):
        ''' Test reload method if file.json not exists '''
        try:
            _store = self.store
            _store.reload()
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False)
