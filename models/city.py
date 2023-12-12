#!/usr/bin/python3
"""
Class city that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city
    """

    state_id = ""
    name = ""