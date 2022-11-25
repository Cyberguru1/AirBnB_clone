#!?usr/bin/python3

""" Represent Class of place"""

from models.base_model import BaseModel

class Place(BaseModel):
    """ 
        Represents Place
    Attributes:
        city_id (str): city of location
        user_id (str): owner
        name (str): name of place
        description (str): short desc about place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guests (int): number of guests we are able to host
        price_by_night (int): price of one night
        latitude (float): latitude part of location
        longitude (float): longitude part of location
        amenity_id (str): amenity it belongs to
    """
    city_id = ""     
    user_id = ""
    name = ""
    description  = ""
    number_rooms = ""  
    number_bathrooms = ""   
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_id = ""
