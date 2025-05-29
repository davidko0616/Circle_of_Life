import random
import os
import time
from enum import Enum
from typing import List, Tuple, Dict, Any

GRID_SIZE=20

class AnimalType(Enum):
    EMPTY:0
    ZEBRA:1
    LION:2

class Animal:
    def __init__(self, x:int, y:int):
        self.x=x
        self.y=y
        self.age=0
        self.alive=True

    def move(self, grid:List[List[AnimalType]], animals:List['Animal'] )->None:
        return NotImplementedError
    
    def breed(self, grid:List[List[AnimalType]], animals:List['Animal'])->None:
        return NotImplementedError
    
    def is_alive(self) -> bool:
        return self.alive
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def die(self) -> None:
        self.alive = False