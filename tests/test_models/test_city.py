#!/usr/bin/python3
'''
    All the tests for the city_model are contained within this implementation.
'''

from models.city import City
from models.base_model import BaseModel
import unittest


class TestCityModel(unittest.TestCase):
    '''
        City class testing.
    '''

    def test_city_inherits(self):
        ''' City class that inherits from BaseModel '''
        city1 = City()
        self.assertIsInstance(city1, BaseModel)

    def test_city_attributes(self):
        ''' City class attributes '''
        att = ["state_id", "name"]
        city1 = City()
        for indx in range(0, len(att)):
            self.assertTrue(att[indx] in city1.__dir__())

    def test_city_state_id_type(self):
        ''' the type of the state_id '''
        city1 = City()
        # get the state_id value from the first_city object
        state_id = getattr(city1, "state_id")
        # checks the type of the state_id value
        self.assertIsInstance(state_id, str)

    def test_city_name_type(self):
        ''' the type of the name '''
        city1 = City()
        # get the name value from the first_city object
        name = getattr(city1, "name")
        # checks the type of the name value
        self.assertIsInstance(name, str)
