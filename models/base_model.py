#!/usr/bin/python3
""" Defining BaseModel colass """
import uuid
import models
from datetime import datetime

class BaseModel:
    """ BaseModel for Classes """

    def __init__(self, *args, *kwargs):
        """
            class constructor

        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()


        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):

        """
            returns a string representation of class
            BaseModel
        """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict___)


    def save(self):
        """
            saves the current instance to model
            storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dict of the instance BaseModel
        """
        object = self.__dict__.copy()
        if (type(self.updated_at) != str):
            object['updated_at'] = self.updated_at.isoformat()
        if type(self.created_at) != str :
            object['created_at'] = self.created_at.isoformat()
        object['__class__'] = self.__class__.__name__
        return object
