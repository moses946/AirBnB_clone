#!/usr/bin/python3
"""
This module contains data definition for a City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class inheriting from BaseModel

    Attr:
        state_id(str): Equals to State.id
        name(str): Name of city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
