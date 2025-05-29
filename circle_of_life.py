import random
import time
from enum import Enum
from typing import List, Tuple, Dict, Any

GRID_SIZE=20

class AnimalType(Enum):
    EMPTY:0
    ZEBRA:1
    LION:2

class Animal:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.age = 0
        self.alive = True
    
    def move(self, grid, animals):
        raise NotImplementedError
    
    def breed(self, grid, animals):
        raise NotImplementedError
    
class Lion(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hunger = 0

    def move(self, grid, animals):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        prey, empty = [], []

