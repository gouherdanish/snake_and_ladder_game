import random

class Dice:
    def __init__(self,start=1,end=6) -> None:
        self.start = start
        self.end = end
    
    def roll(self):
        return random.randint(self.start,self.end)