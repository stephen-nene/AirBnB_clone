#!/usr/bin/python3
'''
  model that contains a FileStorage class that
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import json
import os


class FileStorage:
    ''' Represents the FileStorage class '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        data = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        ''' Deserializes the JSON file to __objects if exists'''
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)

            for val in objdict.values():
                class_name = val["__class__"]
                del val["__class__"]
                self.new(eval(class_name)(**val))

        except FileNotFoundError:
            pass

