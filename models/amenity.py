#!/usr/bin/python3
"""
This module contains data definition for an amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Definition for amenities.

    Attrs:
        name(str): name of amenity
    """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.name = ""
