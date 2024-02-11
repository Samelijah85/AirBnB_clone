#!/usr/bin/python3
"""
Implements a Class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects

        Returns:
            All objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (object): The object to add
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as jf:
            json.dump(serialized_objs, jf)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as jf:
                serialized_objs = json.load(jf)
            for key, obj_dict in serialized_objs.items():
                self.new(eval(key.split(".")[0])(**obj_dict))
        except FileNotFoundError:
            pass
