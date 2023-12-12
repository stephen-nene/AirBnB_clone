#!/usr/bin/python3
'''
    All the tests for the state_model are contained within this implementation.
'''

from models.state import State
from models.base_model import BaseModel
import unittest


class TestStateModel(unittest.TestCase):
    '''
        State class testing.
    '''

    def test_state_inherits(self):
        ''' State class that inherits from BaseModel '''
        state1 = State()
        self.assertIsInstance(state1, BaseModel)

    def test_state_attributes(self):
        ''' State class attributes '''
        att = ["name"]
        state1 = State()
        for indx in range(0, len(att)):
            self.assertTrue(att[indx] in state1.__dir__())

    def test_state_name_type(self):
        ''' The type of the name '''
        state1 = State()
        # get the name value from the first_state object
        name = getattr(state1, "name")
        # checks the type of the name value
        self.assertIsInstance(name, str)
