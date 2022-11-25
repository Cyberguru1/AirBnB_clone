#!/usr/bin/python3

""" Defines City Class  """

from models.base_model import BaseModel

class City(BaseModel):
    """ Represents City
    Attributes:
        state_id (str): id of state
        name  (str): name of the city
    """
    state_id = ""
    name = ""