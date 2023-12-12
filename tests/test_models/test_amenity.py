#!/usr/bin/python3
'''
    All the tests for the amenity_model are contained
      within this implementation.
'''

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenityModel(unittest.TestCase):
    '''
        Amenity class testing.
    '''

    def test_amenity_inherits(self):
        ''' Amenity class that inherits from BaseModel '''
        amenity1 = Amenity()
        self.assertIsInstance(amenity1, BaseModel)

    def test_amenity_attributes(self):
        ''' Amenity class attributes '''
        att = ["name"]
        amenity1 = Amenity()
        for indx in range(0, len(att)):
            self.assertTrue(att[indx] in amenity1.__dir__())

    def test_amenity_name_type(self):
        ''' The type of the name '''
        amenity1 = Amenity()
        # get the name value from the first_Amenity object
        name = getattr(amenity1, "name")
        # checks the type of the name value
        self.assertIsInstance(name, str)
