#!/usr/bin/python3
"""
This module contains class console that defines the command intepreter for the project.
"""
import cmd
from models.amenity import Amenity
from models.base_models import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import re


class_names = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

objects = storage.all()

class HBNBCommand(cmd.Cmd):
    """
    Console class inheriting from the Cmd superclass
    """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """"
        Creates a new instance of BaseModel and saves it to json file and prints the id
        """
        if arg is not None:
            if arg in class_names.keys():
                new_model = class_names[arg]()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.

        Vars:
            arg_list(list): Argument vector
        """
        arg_list = arg.split(' ')
        if len(arg_list) == 0 or arg_list[0] == '':
            print("** class name missing **")
        elif arg_list[0] not in class_names.keys():
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif arg_list[0]+"."+arg_list[1] not in objects.keys():
            print("** no instance found **")
        else:
            print(class_names[arg_list[0]](**objects[arg_list[0]+"."+arg_list[1]]))

    def do_destroy(self, args):
        """
        Deletes an instance based on classname and id
        
        Vars:
            arg_list(list): Argument vector
        """
        arg_list = args.split(" ")
        if len(arg_list) == 0 or arg_list[0] == '':
            print("** class name missing **")
        elif arg_list[0] not in class_names.keys():
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif arg_list[0]+"."+arg_list[1] not in objects.keys():
            print("** no instance found **")
        else:
            del objects[arg_list[0]+"."+arg_list[1]]
            storage.__objects = objects
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based on the classname

        Vars:
            str_rep(list): A list of string representation of all instances
        """
        arg = arg.split(' ')
        if len(arg) > 0 and arg[0] != '':
            if arg[0] in class_names.keys():
                str_rep = []
                for obj_key in objects.keys():
                    if obj_key.split('.')[0] == arg[0]:
                        str_rep.append(str(objects[obj_key]))
                print(str_rep)
            else:
                print("** class doesn't exist **")
        else:
            str_rep = []
            for obj_key in objects.keys():
                str_rep.append(str(objects[obj_key]))
            print(str_rep)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute

        """
        arg_list = args.split(" ")
        if len(arg_list) == 0 or arg_list[0] == '':
            print("** class name missing **")
        elif arg_list[0] not in class_names.keys():
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif arg_list[0]+"."+arg_list[1] not in objects.keys():
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            obj_to_update = class_names[arg_list[0]](**objects[arg_list[0]+"."+arg_list[1]])
            setattr(obj_to_update, arg_list[2], ' '.join(arg_list[3:]))
            del objects[arg_list[0]+"."+arg_list[1]]
            storage.__objects = objects
            storage.new(obj_to_update)
            obj_to_update.save()

    @staticmethod
    def count(arg):
        if arg in class_names.keys():
            str_rep = []
            for obj_key in objects.keys():
                if obj_key.split('.')[0] == arg:
                    str_rep.append(str(objects[obj_key]))
            print(len(str_rep))

    def default(self, args):
        """
        Default method to accept input in the form <class name>.<method>() or print error message on unknown command.

        Vars:
            cl_name: Class Name
            method: Method to apply

        """
        try:
            cl_name, method = args.split('.')
            if cl_name in class_names.keys():
                method = method.strip("()")
                if method == "all":
                    self.do_all(cl_name)
                elif method == "count":
                    self.count(cl_name)
                elif re.search("show\(\"[\S]+\"", method):
                    method, id = method.split('(')
                    id = id.strip('"')
                    self.do_show(str(cl_name + " " + id))
                elif re.search("destroy\(\"[\S]+\"", method):
                    method, id = method.split('(')
                    id = id.strip('"')
                    self.do_destroy(str(cl_name + " " + id))
                elif re.search("update\(\"[\S]+,", method):
                    method, attrs = method.split('(')
                    attrs = attrs.split(",")
                    if '{' not in attrs[1]:
                        attrs = [attr.strip(' "') for attr in attrs]
                        self.do_update(str(cl_name + " " + " ".join(attrs)))
                    elif "{" in attrs[1]:
                        attr_dict = eval(','.join(attrs[1:]))                        
                        for key, val in attr_dict.items():
                            arg = str(cl_name + " " + attrs[0].strip('"') + " " + key + " " + val)
                            self.do_update(arg)

            else:
                print(f"** unknown syntax: {args} **")               
        except Exception:
            print(f"** unknown syntax: {args} **")
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
