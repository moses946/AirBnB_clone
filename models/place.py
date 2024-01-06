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
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
