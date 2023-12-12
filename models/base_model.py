#!/usr/bin/python3
'''
    This module contains the definition of the BaseModel class
'''

import uuid
import datetime
import models


class BaseModel:
    '''
        class BaseModel that defines all common attributes/methods
            for other classes
    '''

    def __init__(self, *args, **kwargs):
        ''' Public instance attributes '''
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            kwargs['created_at'] = datetime.datetime.strptime(
                kwargs['created_at'],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs['updated_at'] = datetime.datetime.strptime(
                kwargs['updated_at'],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        '''
            Return a string that representation of BaseModel class
        '''
        s = "[{}] ({}) {}"
        return s.format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        '''
            updates the public instance attribute updated_at
                with the current datetime
        '''
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            returns a dictionary containing all keys/values
              of __dict__ of the instance
        '''
        dct_instance = self.__dict__.copy()
        dct_instance['__class__'] = self.__class__.__name__
        dct_instance['created_at'] = self.created_at.isoformat()
        dct_instance['updated_at'] = self.updated_at.isoformat()
        return dct_instance