#!/usr/bin/python3
'''
    All the tests for the place_model are contained within this implementation.
'''

from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceModel(unittest.TestCase):
    '''
        Place class testing.
    '''

    def test_place_inherits(self):
        ''' Place class that inherits from BaseModel '''
        place1 = Place()
        self.assertIsInstance(place1, BaseModel)

    def test_place_attributes(self):
        ''' Place class attributes '''
        att = [
            "city_id",
            "user_id",
            "name",
            "description",
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            "latitude",
            "longitude",
            "amenity_ids"
        ]
        place1 = Place()
        for indx in range(0, len(att)):
            self.assertTrue(att[indx] in place1.__dir__())

    def test_place_cityId_type(self):
        ''' The type of the cityId '''
        place1 = Place()
        # get the cityId value from the first_place object
        city_id = getattr(place1, "city_id")
        # checks the type of city_id value
        self.assertIsInstance(city_id, str)

    def test_place_userId_type(self):
        ''' Type of the userId '''
        place1 = Place()
        # get the user_id value from the first_place object
        user_id = getattr(place1, "user_id")
        # checks the type of user_id value
        self.assertIsInstance(user_id, str)

    def test_place_name_type(self):
        ''' The type of the name '''
        place1 = Place()
        # get the name value from the first_place object
        name = getattr(place1, "name")
        # checks the type of name value
        self.assertIsInstance(name, str)

    def test_place_desc_type(self):
        ''' The type of the description '''
        place1 = Place()
        # get the description value from the first_place object
        descr = getattr(place1, "description")
        # checks the type of the description value
        self.assertIsInstance(descr, str)

    def test_place_nr_type(self):
        ''' The type of the number_rooms '''
        place1 = Place()
        # get the number_rooms value from the first_place object
        num_rooms = getattr(place1, "number_rooms")
        # checks the type of the number_rooms value
        self.assertIsInstance(num_rooms, int)

    def test_place_nb_type(self):
        ''' The type of the number_bathrooms '''
        place1 = Place()
        # get the number_bathrooms value from the first_place object
        num_bathrooms = getattr(place1, "number_bathrooms")
        # checks the type of the number_bathrooms value
        self.assertIsInstance(num_bathrooms, int)

    def test_place_mg_type(self):
        ''' The type of the max_guest '''
        place1 = Place()
        # get the max_guest value from the first_place object
        mx_guest = getattr(place1, "max_guest")
        # checks the type of the max_guest value
        self.assertIsInstance(mx_guest, int)

    def test_place_pbn_type(self):
        ''' The type of the price_by_night '''
        place1 = Place()
        # get the price_by_night value from the first_place object
        pr_by_night = getattr(place1, "price_by_night")
        # checks the type of the price_by_night value
        self.assertIsInstance(pr_by_night, int)

    def test_place_latitude_type(self):
        ''' The type of the latitude '''
        place1 = Place()
        # get the latitude value from the first_place object
        lat = getattr(place1, "latitude")
        # checks the type of the latitude value
        self.assertIsInstance(lat, float)

    def test_place_longitude_type(self):
        ''' The type of the longitude '''
        place1 = Place()
        # get the longitude value from the first_place object
        long = getattr(place1, "longitude")
        # checks the type of the longitude value
        self.assertIsInstance(long, float)

    def test_place_amenity_ids_type(self):
        ''' The type of the amenity_ids '''
        place1 = Place()
        # get the amenity_ids value from the first_place object
        amen_ids = getattr(place1, "amenity_ids")
        # checks the type of the amenity_ids value
        self.assertIsInstance(amen_ids, list)
