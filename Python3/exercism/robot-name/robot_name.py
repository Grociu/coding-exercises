"""
This program creates a class of robots.
Robots are born with no name.
On boot they get assigned a random, unique name 
in format like AA001. 2 uppercase letters, 3 numbers.
You can to reset a robot, and assign it a new name.
"""

from random import randint

# This is a list of all active robot names. Used to control uniqueness of names.
all_robot_names = []

def random_letter():
    """This generates a random uppercase letter, this can probably be done better."""
    alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = randint(0,len(alphabeth)-1)
    return alphabeth[num]

class Robot(object):
    def __init__(self):
        self.uniquename()

    def name_gen(self):
        """This function generates a random name in the AA001 format"""
        random_name = "".join([random_letter(),random_letter(),str(randint(0,9)),
                         str(randint(0,9)),str(randint(0,9))])
        return random_name

    def uniquename(self):
        """This function checks the uniqueness of a robot name"""
        self.name = self.name_gen()
        while self.name in all_robot_names:
            self.name = self.name_gen()
        else: 
            all_robot_names.append(self.name)    

    def reset(self):
        """On a reset, a robot gets a new name, if that name is on the list,
           it gets another"""
        #all_robot_names.remove(self.name) <== name returns to availible name pool?
        self.uniquename()