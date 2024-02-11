#!/usr/bin/python3
"""Creates a User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
