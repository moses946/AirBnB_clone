#!/usr/bin/python3
"""
This module contains data definition for a place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Definition for a place/BnB

    Attr:
        city_id(str): Equals City.id
        user_id(str): Equals User.id
        name(str): name of place
        description(str): Short description of a place
        number_rooms(int): Number of rooms
        number_bathrooms(int): Number of bathrooms
        max_guests(int): Maximum no of guests
        price_by_night(int): Cost per night
        latitude(float)
        longitude(float)
        amenity_ids(list): List of Amenity.id
    """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.city_id = ''
        self.user_id = ''
        self.name = ''
        self.description = ''
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guests = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
