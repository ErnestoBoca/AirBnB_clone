#!/usr/bin/python3
"""This module defines the command interpreter for the project"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, s):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def do_EOF(self, line):
        print()
        return True

    help_EOF = help_quit

    def classes(self):
        return {"BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}

    def check(self, args, max_args):
        list_args = args.split()

        size = len(list_args)
        for i in range(max_args):
            if i == 0:
                if size == i:
                    print("** class name missing **")
                    return False
                if list_args[i] not in self.classes().keys():
                    print("** class doesn't exist **")
                    return False

            if i == 1:
                if size == i:
                    print("** instance id missing **")
                    return False
                objects = storage.all()
                obj_id = list_args[0] + "." + list_args[1]
                if obj_id not in objects.keys():
                    print("** no instance found **")
                    return False

            if i == 2:
                if size == i:
                    print("** attribute name missing **")
                    return False

            if i == 3:
                if size == i:
                    print("** value missing **")
                    return False

        return True

    def do_create(self, args):
        if self.check(args, 1):
            new_obj = self.classes()[args]()
            storage.save()
            print(new_obj.id)

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it" +
              "(to the JSON file) and prints the id. Ex: $ create BaseModel")
        print()

    def do_show(self, args):
        if self.check(args, 2):
            list_args = args.split()
            obj_id = list_args[0] + "." + list_args[1]
            dict_obj = storage.all()
            print(dict_obj[obj_id])

    def help_show(self):
        print("Prints the string representation of an instance based on the" +
              "class name and id. Ex: $ show BaseModel 1234-1234-1234")
        print()

    def do_destroy(self, args):
        if self.check(args, 2):
            list_args = args.split()
            obj_id = list_args[0] + "." + list_args[1]
            dict_obj = storage.all()
            del dict_obj[obj_id]
            storage.save()

    def help_destroy(self):
        print("Deletes an instance based on the class name and id" +
              "(save the change into the JSON file)." +
              "Ex: $ destroy BaseModel 1234-1234-1234.")
        print()

    def do_all(self, args):
        list_obj = []
        dict_obj = storage.all()
        if args:
            if self.check(args, 1):
                for value in dict_obj.values():
                    if value.__class__.__name__ == args:
                        list_obj.append(str(value))
        else:
            for value in dict_obj.values():
                list_obj.append(str(value))
        if list_obj:
            print(list_obj)

    def help_all(self):
        print("Prints all string representation of all instances based" +
              "or not on the class name.")
        print()

    def do_update(self, args):
        if self.check(args, 4):
            list_args = args.split()
            dict_obj = storage.all()
            obj_id = list_args[0] + "." + list_args[1]
            obj = dict_obj[obj_id]
            attr = list_args[2]
            value = list_args[3]

            if '"' in value:
                value = value.replace('"', '')
            else:
                try:
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                except ValueError:
                    pass

            if hasattr(obj, attr):
                value = type(getattr(obj, attr))(value)

            setattr(obj, attr, value)
            storage.save()

    def help_update(self):
        print("Updates an instance based on the class name and id by " +
              "adding or updating attribute(save the change into the " +
              "JSON file).Ex: $ update BaseModel 1234-1234-1234 email " +
              "'aibnb@mail.com' .")
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
