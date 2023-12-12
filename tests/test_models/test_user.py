#!/usr/bin/python3
'''
    All the tests for the user_model are contained within this implementation.
'''

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUserModel(unittest.TestCase):
    '''
        User class testing.
    '''

    def test_user_inherits(self):
        ''' User class that inherits from BaseModel '''
        user1 = User()
        self.assertIsInstance(user1, BaseModel)

    def test_user_attributes(self):
        ''' User class attributes '''
        att = ["email", "password", "first_name", "last_name"]
        user1 = User()
        for idx in range(0, len(att)):
            self.assertTrue(att[idx] in user1.__dir__())

    def test_user_fname_type(self):
        ''' user first_name '''
        user1 = User()
        # get first_name value from first_user object
        user1 = getattr(user1, "first_name")
        # checks the type of first_name value
        self.assertIsInstance(user1, str)

    def test_user_lname_type(self):
        ''' user last_name '''
        user1 = User()
        # get last_name value from first_user object
        last_user = getattr(user1, "last_name")
        # checks the type of last_name value
        self.assertIsInstance(last_user, str)

    def test_user_email_type(self):
        ''' user email '''
        user1 = User()
        # get email value from first_user object
        email = getattr(user1, "email")
        # checks the type of email value
        self.assertIsInstance(email, str)

    def test_user_password_type(self):
        ''' user password '''
        user1 = User()
        # get password value from first_user object
        password = getattr(user1, "password")
        # checks the type of password value
        self.assertIsInstance(password, str)
