"""
This contains the Character class, that generates 
a random DnD character to given specification
"""

from random import randint

def modifier(attribute):
    """This generates a modifier for an attribute."""
    """I think the test wants this to be outside the Character class"""
    return (attribute - 10) // 2

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
    
    def ability(self):
        """This function generates a random ability score"""
        rolls = [randint(1,6) for x in range(0,4)]
        rolls.remove(min(rolls))
        return sum(rolls)