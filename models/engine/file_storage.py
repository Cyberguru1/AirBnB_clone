#!/usr/bin/python3
"""
    FileStorage engine
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
        Storing files through
        Serialization and Deserialization
    Attributes:
        _file_path(str): path to json file objects
        _objects(dict): dictionary of all objects
    """
    __file_path = "file.json"
    __objects = dict({})

    def all(self):
        """ returns all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets __objects with new obj"""
        Ocname = obj.__class__.__name__
        FileStorage.__objects["{},{}".format(Ocname, obj.id)] = obj

    def save(self):
        """ serializes the  __objects to json"""
        Odict = FileStorage.__objects
        Ob_dict = {obj: Odict[obj].to_dict() for obj in Odict.keys()}
        with open(FileStorage.__File_path, "w") as f:
            json.dump(Ob_dict, f)

    def reload(self):
        try:
            with open(FileStorage, __file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
