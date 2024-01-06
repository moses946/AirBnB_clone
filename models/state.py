#!/usr/bin/python3
"""
This module contains data definition for a state
"""
from models.base_models import BaseModel


class State(BaseModel):
    """
    State class inheriting from BaseModel Class

    Attr:
        name(str): Name of state
    """
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        self.name = ''
