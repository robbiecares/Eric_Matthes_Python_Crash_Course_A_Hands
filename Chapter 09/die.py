import random

class Die:
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        roll = random.randint(1,self.sides)
        return roll



