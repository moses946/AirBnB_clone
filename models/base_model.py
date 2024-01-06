#!/usr/bin/python3
"""
BaseModel module defining the base model class.
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Class defining all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Print the class name, id and dictionary representation of an instance
        """
        return f"[{type(self).__name__}]({self.id}){vars(self)}"

    def save(self):
        """
        Update the updated_at attribute
        """
        key = str(type(self).__name__) + "." + self.id
        if key in storage.all():
            del storage.all()[key]
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance.
        """
        instance_dict = {}
        for key, val in self.__dict__.items():
            instance_dict[key] = val
        instance_dict["__class__"] = type(self).__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
