#!/usr/bin/python3
'''
    console.py that contains the entry point of the command interpreter
'''
import cmd
import json
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parser(input_string):
    curly_match = re.search(r"\{(.*?)\}", input_string)
    bracket_match = re.search(r"\[(.*?)\]", input_string)

    if curly_match is None:
        if bracket_match is None:
            return [item.strip(",") for item in split(input_string)]
        else:
            lexer = split(input_string[:bracket_match.span()[0]])
            result_list = [item.strip(",") for item in lexer]
            result_list.append(bracket_match.group())
            return result_list
    else:
        lexer = split(input_string[:curly_match.span()[0]])
        result_list = [item.strip(",") for item in lexer]
        result_list.append(curly_match.group())
        return result_list


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    own_classes = [
        'BaseModel', 'User', 'State', 'Review', 'Place', 'City', 'Amenity'
    ]

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", line)
        if match is not None:
            args = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                cmd_line = [args[1][:match.span()[0]], match.group()[1:-1]]
                if cmd_line[0] in arg_dict.keys():
                    call = "{} {}".format(args[0], cmd_line[1])
                    return arg_dict[cmd_line[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return False

    def emptyline(self):
        '''empty line command'''
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program on End-of-File input (Ctrl+D or Ctrl+Z)"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel & saves it"""
        args = parser(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.own_classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on class name & id
        """
        args = parser(line)
        all_objcts = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.own_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all_objcts:
            print("** no instance found **")
        else:
            print(all_objcts["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name & id"""
        args = parser(line)
        all_objcts = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.own_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) \
                not in all_objcts.keys():
            print("** no instance found **")
        else:
            del all_objcts["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation
        of all instances based or not on the class name
        """
        args = parser(line)
        if len(args) > 0 and args[0] not in HBNBCommand.own_classes:
            print("** class doesn't exist **")
        else:
            objcts = []
            for obj in storage.all().values():
                if len(args) > 0 and \
                        args[0] == obj.__class__.__name__:
                    objcts.append(obj.__str__())
                elif len(args) == 0:
                    objcts.append(obj.__str__())
            print(objcts)

    def do_update(self, line):
        """
        Updates an instance based on the class name, id,
        and attribute name with a new attribute value.
        """
        args = parser(line)
        all_objs = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.own_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in all_objs.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            ob = all_objs["{}.{}".format(args[0], args[1])]
            if args[2] in ob.__class__.__dict__.keys():
                valtype = type(ob.__class__.__dict__[args[2]])
                ob.__dict__[args[2]] = valtype(args[3])
            else:
                ob.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            ob = all_objs["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in ob.__class__.__dict__.keys() and
                        type(ob.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(ob.__class__.__dict__[key])
                    ob.__dict__[key] = valtype(value)
                else:
                    ob.__dict__[key] = value
        storage.save()

    def do_count(self, line):
        """Retrieve the number of instances of a class: <class name>.count()"""
        args = parser(line)
        cntr = 0
        for ob in storage.all().values():
            if args[0] == ob.__class__.__name__:
                cntr += 1
        print(cntr)


if __name__ == '__main__':
    HBNBCommand().cmdloop()