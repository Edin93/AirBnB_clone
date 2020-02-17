#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
import inspect
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    Command processor
    """

    prompt = '(hbnb) '

    @staticmethod
    def check_class(x):
        """Check if x is a class."""
        try:
            r = inspect.isclass(eval(x))
            return r
        except:
            return False

    def do_EOF(self, line):
        """
        End-of-file marker
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit the command line
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """
        Create an instance of BaseModel
        Usage: create <class Name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                my_class = eval(args[0])()
                my_class.save()
                print("{}".format(my_class.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id.
        Usage: show <class Name> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    objs = storage.all()
                    if key in objs:
                        print(objs[key])
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage: Destroy <class Name> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in storage.all():
                        storage.del_key(key)
                        storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on
        the class name.
        Usage: all <class Name> or all
        """
        args = line.split()
        objs = []
        if len(args) == 0:
            for k, v in storage.all().items():
                objs.append(str(v))
            print(objs)
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    obj_keys = k.split('.')
                    if obj_keys[0] == args[0]:
                        objs.append(str(v))
                print(objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key in storage.all():
                        if len(args) == 2:
                            print('** attribute name missing **')
                        elif len(args) == 3:
                            print('** value missing **')
                        else:
                            storage.update_obj(key, args[2], args[3])
                            storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    import sys

    CtrlC = False
    while CtrlC is not True:
        try:
            HBNBCommand().cmdloop()
            CtrlC = True
        except KeyboardInterrupt:
            sys.stdout.write('\n')
