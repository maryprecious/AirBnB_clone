#!/usr/bin/python3
""" This is the Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review and to store review information """
    place_id = ""
    user_id = ""
    text = ""
