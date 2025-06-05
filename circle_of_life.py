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

class Zebra(Animal):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.breed_timer = 3

    def move(self, grid, animals):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(directions)

        empty = []
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= ny < len(grid) and 0 <= nx len(grid[0]):
                if grid[ny][nx] is None:
                    empty.append((nx, ny))

        if empty:
            new_x, new_y = random.choice(empty)
            grid[self.y][self.x] = None
            self.x, self.y = new_x, new_y
            grid[self.y][self.x] = self

    def breed(self, grid, animals):
        self.breed_timer -= 1
        if self.breed_timer > 0:
            return

        self.breed_timer = 3  # Reset breeding timer
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] is None:
                    baby = Zebra(nx, ny)
                    grid[ny][nx] = baby
                    animals.append(baby)
                    break

class Lion(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hunger = 0

    def move(self, grid, animals):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        prey, empty = [], []

