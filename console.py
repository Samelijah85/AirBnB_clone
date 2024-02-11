#!/usr/bin/python3
"""Implements the HBNB console"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

classes = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter which inherits from cmd module"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_create(self, arg):
        """
        Create a new class instance

        Usage: create <class name>
        """
        args = custom_cmd_parser(arg)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_id = eval(args[0])().id
            print(f'{new_id}')
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id

        Usage: show <class name> <id>
        """
        all_obj = storage.all()
        args = custom_cmd_parser(arg)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif "{}.{}".format(args[0], args[1]) not in all_obj:
            print('** no instance found **')
        else:
            print(all_obj["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """
        all_obj = storage.all()
        args = custom_cmd_parser(arg)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif "{}.{}".format(args[0], args[1]) not in all_obj.keys():
            print('** no instance found **')
        else:
            del all_obj["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name

        Usage: all <class name> or all
        """
        args = custom_cmd_parser(arg)
        if (len(args) > 0):
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            object_list = [
                str(obj) for obj in storage.all().values()
                if obj.__class__.__name__ == class_name
            ]
        else:
            object_list = [str(obj) for obj in storage.all().values()]

        print(object_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        all_obj = storage.all()
        args = custom_cmd_parser(arg)

        if len(args) == 0:
            print('** class name missing **')
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print('** instance id missing **')
            return

        instance_id = f"{class_name}.{args[1]}"
        if instance_id not in all_obj.keys():
            print('** no instance found **')
            return

        if len(args) == 2:
            print('** attribute name missing **')
            return

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print('** value missing **')
                return

        obj = all_obj[instance_id]
        attr_name = args[2]
        if len(args) == 4:
            attr_value = args[3]
            if attr_name in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[attr_name])
                obj.__dict__[attr_name] = val_type(attr_value)
            else:
                obj.__dict__[attr_name] = attr_value
        else:
            for key, value in eval(attr_name).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(value)
                else:
                    obj.__dict__[key] = value

        storage.save()

    def emptyline(self):
        """Does not execute anything"""
        pass

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class

        Usage: <class name>.count()
        """
        args = custom_cmd_parser(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """
        Called when the command prefix is not recognized
        """

        command_mapping = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        args = arg.split('.', 1)
        if len(args) == 2:
            search = re.search(r"\((.*?)\)", args[1])
            if search:
                command = [args[1][:search.span()[0]], search.group()[1:-1]]
                if command[0] in command_mapping.keys():
                    call = f"{args[0]} {command[1]}"
                    return command_mapping[command[0]](call)

        print(f"*** Unknown syntax: {arg}")


def custom_cmd_parser(arg):
    """
    Parse command arguments to a list
    """
    curly_match = re.search(r"\{(.*?)\}", arg)
    bracket_match = re.search(r"\[(.*?)\]", arg)

    if curly_match is None:
        if bracket_match is None:
            return [item.strip(",") for item in split(arg)]
        else:
            tokens = split(arg[:bracket_match.span()[0]])
            result_list = [item.strip(",") for item in tokens]
            result_list.append(bracket_match.group())
            return result_list
    else:
        tokens = split(arg[:curly_match.span()[0]])
        result_list = [item.strip(",") for item in tokens]
        result_list.append(curly_match.group())
        return result_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()
