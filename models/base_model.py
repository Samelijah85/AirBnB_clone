#!/usr/bin/python3
"""
Script that implements a class BaseModel that defines all common
attributes/methods for other classes.
"""
import uuid
from datetime import datetime


class BaseModel:
    """A BaseModel class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class

        Args:
            args (list): A list of arguments
            kwargs (dict): Key-value pair arguments
        """
        for key, value in kwargs.items():
            if key != "__class__":
                if key == "created_at":
                    self.__dict__['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.__dict__['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "id":
                    setattr(self, key, str(value))
                else:
                    setattr(self, key, value)
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
            )

    def save(self):
        """Updates the attribute 'update_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of '__dict__'
        of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
