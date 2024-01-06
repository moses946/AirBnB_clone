#!/usr/bin/python3
"""
This module contais class FileStorage to serialize and deserialize data.
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    Attr:
        __file_path: Path to a JSON file
        __objects: Dictionary storing all objects written to the JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self, file_path=None):
        """
        Changes default file_path while running tests
        """
        if file_path:
            self.__file_path = file_path

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object to the dictionary __objects.
        """
        key = str(type(obj).__name__) + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to a JSON file

        Vars:
            json_string(str): JSON string created from __objects
            file: Open JSON file buffer
        """
        json_string = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as file:
            try:
                file.write(json_string)
                file.close()
            except IOError:
                print(f"Unable to write to file: {self.__file}")

    def reload(self):
        """
        Deserializes JSON object from file to __objects if file exists
        
        Vars:
            json_string(str): JSON string loaded from file
            file: Open JSON file buffer
        """
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
                file.close()    
        except FileNotFoundError:
            pass
