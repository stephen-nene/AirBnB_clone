#!/usr/bin/python3
'''
    All the tests for the base_model are contained within this implementation.
'''

from models.base_model import BaseModel
import sys
import unittest
import time
from io import StringIO
import datetime


class TestBaseModel(unittest.TestCase):
    '''
        The BaseModel class testing.
    '''

    def setUp(self):
        ''' Create a new model from the BaseModel '''
        self.new_model = BaseModel()
        self.new_model.name = "youssef nasrallah"

    def test_obj_type(self):
        ''' Object type '''
        # create some objects from BaseModel for testing
        object0 = BaseModel()
        object1 = BaseModel()
        object2 = BaseModel()
        # Checks that the type of the obj is BaseModel
        self.assertEqual(type(object0), BaseModel)
        self.assertEqual(type(object1), BaseModel)
        self.assertEqual(type(object2), BaseModel)
        # checks that the type of eny objects is BaseModel
        self.assertEqual(type(object0), type(object1))
        self.assertEqual(type(object1), type(object2))
        self.assertEqual(type(object2), type(object0))

    def test_id_type(self):
        ''' Id type '''
        # create some objects from BaseModel for testing
        object0 = BaseModel()
        object1 = BaseModel()
        object2 = BaseModel()
        # Checks that the type of the id is string
        self.assertEqual(type(object0.id), type("string"))
        self.assertEqual(type(object1.id), type("string"))
        self.assertEqual(type(object2.id), type("string"))

    def test_id_values(self):
        ''' Id value '''
        # create some objects from BaseModel for testing
        object0 = BaseModel()
        object1 = BaseModel()
        object2 = BaseModel()
        # checks that eny object has a uniq id
        self.assertNotEqual(object0.id, object1.id)
        self.assertNotEqual(object1.id, object2.id)
        self.assertNotEqual(object2.id, object0.id)

    def test_name_value(self):
        ''' Change name value '''
        self.new_model.name = "Redwan Ben Yechou"
        self.assertEqual(self.new_model.name, "Redwan Ben Yechou")

    def test_date_time_equal(self):
        ''' Checks if created_at equal updated_at '''
        obj = BaseModel()
        # first let's checks new_model date and time
        self.assertNotEqual(
                self.new_model.created_at, self.new_model.updated_at
                )
        # second let's checks our obj
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_save_method(self):
        ''' Save method '''
        last_update = self.new_model.updated_at
        time.sleep(1)
        self.new_model.save()
        self.assertNotEqual(last_update, self.new_model.updated_at)

    def test_str_method(self):
        ''' t__str__ method '''
        copy = sys.stdout
        _id = self.new_model.id
        cap_output = StringIO()
        sys.stdout = cap_output
        print(self.new_model)
        _lst = cap_output.getvalue().split(" ")
        self.assertEqual(_lst[0], "[BaseModel]")
        self.assertEqual(_lst[1], "({})".format(_id))
        sys.stdout = copy

    def test_to_dict_out_type(self):
        ''' Test : checks the type of output for to_dict method '''
        obj = {}
        self.assertEqual(type(obj), type(self.new_model.to_dict()))

    def test_to_dict_class_name(self):
        ''' Checks class name value in dict '''
        class_name = "BaseModel"
        self.assertEqual(class_name, self.new_model.to_dict()['__class__'])

    def test_to_dict_created_at(self):
        ''' Checks created_at type in dict '''
        str = "string"
        self.assertEqual(type(str), type(self.new_model.to_dict()['created_at']))

    def test_to_dict_updated_at(self):
        ''' Checks updated_at type in dict '''
        str = "string"
        self.assertEqual(type(str), type(self.new_model.to_dict()['updated_at']))

    def test_kwargs(self):
        ''' Test : instances created using kwargs '''
        object0 = self.new_model.to_dict()
        object1 = BaseModel(**object0)
        self.assertEqual(self.new_model.id, object1.id)

    def test_created_at_type(self):
        ''' Checks the type of created_at '''
        object0 = self.new_model.to_dict()
        object1 = BaseModel(**object0)
        result = isinstance(object1.created_at, datetime.datetime)
        self.assertTrue(result)

    def test_updated_at_type(self):
        ''' Checks the type of updated_at '''
        object0 = self.new_model.to_dict()
        object1 = BaseModel(**object0)
        rslt = isinstance(object1.updated_at, datetime.datetime)
        self.assertTrue(rslt)

    def test_dict(self):
        ''' Compare two dict '''
        object0_dict = self.new_model.to_dict()
        object1 = BaseModel(**object0_dict)
        object1_dict = object1.to_dict()
        self.assertEqual(object0_dict, object1_dict)

    def test_compare_dict(self):
        ''' Compare two dict '''
        object0_dict = self.new_model.to_dict()
        object1 = BaseModel(object0_dict)
        self.assertNotEqual(object1, self.new_model)
