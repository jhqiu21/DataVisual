# a die class to simulate rolling a die
from random import randint

class Die:
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    
    # return a random integer between 1 and nums_sides to simulate rolling a die
    def roll(self):
        return randint(1, self.num_sides)