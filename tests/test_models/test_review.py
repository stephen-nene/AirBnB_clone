#!/usr/bin/python3
'''
    All the tests for the review_model are
      contained within this implementation.
'''

from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReviewModel(unittest.TestCase):
    '''
        Review class testing.
    '''

    def test_review_inherits(self):
        ''' Review class that inherits from BaseModel '''
        review1 = Review()
        self.assertIsInstance(review1, BaseModel)

    def test_review_attributes(self):
        ''' Review class attributes '''
        att = ["place_id", "user_id", "text"]
        review1 = Review()
        for indx in range(0, len(att)):
            self.assertTrue(att[indx] in review1.__dir__())

    def test_review_place_id_type(self):
        ''' The type of the place_id '''
        review1 = Review()
        # get the place_id value from the first_review object
        place_id = getattr(review1, "place_id")
        # checks the type of the place_id value
        self.assertIsInstance(place_id, str)

    def test_review_user_id_type(self):
        ''' The type of the user_id '''
        review1 = Review()
        # get the user_id value from the first_review object
        us_id = getattr(review1, "user_id")
        # checks the type of the user_id value
        self.assertIsInstance(us_id, str)

    def test_review_text_type(self):
        ''' The type of the text '''
        review1 = Review()
        # get the text value from the first_review object
        txt = getattr(review1, "text")
        # checks the type of the text value
        self.assertIsInstance(txt, str)
