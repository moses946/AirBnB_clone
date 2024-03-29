#!/usr/bin/python3
"""
This module contains data definition for a state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inheriting from BaseModel Class

    Attr:
        name(str): Name of state
    """
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
