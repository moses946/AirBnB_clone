#!/usr/bin/python3
"""
This module contains definition for a single user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inheriting from BaseModel class

    Attr:
        email(string): user email
        password(string): user password
        first_name(string): user's firstname
        last_name(string): user's lastname
    """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
