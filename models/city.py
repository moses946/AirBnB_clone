#!/usr/bin/python3
"""
This module contains data definition for a City
"""
from models.base_models import BaseModel


class City(BaseModel):
    """
    City Class inheriting from BaseModel

    Attr:
        state_id(str): Equals to State.id
        name(str): Name of city
    """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.state_id = ""
        self.name = ""
