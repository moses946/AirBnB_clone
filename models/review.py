#!/usr/bin/python3
"""
This module contains data definition for a review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Definition for a review

    Attr:
        place_id(str): Equals to Place.id
        user_id(str): Equals to User.id
        text(str)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.place_id = ''
        self.user_id = ''
        self.text = ''
