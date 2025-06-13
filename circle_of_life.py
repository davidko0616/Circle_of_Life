import random
import os
import time
from enum import Enum
from typing import List, Tuple, Dict, Any

GRID_SIZE=50

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
    def move(self, grid, animals):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        empty = [(self.x+dx, self.y+dy) for dx, dy in directions
                if 0 <= self.x+dx < GRID_SIZE and 0 <= self.y+dy < GRID_SIZE
                and grid[self.x+dx][self.y+dy] == AnimalType.EMPTY]

        if empty:
            new_x, new_y = random.choice(empty)
            grid[self.y][self.x] = AnimalType.EMPTY
            self.x, self.y = new_x, new_y
            grid[self.y][self.x] = AnimalType.ZEBRA

        self.age += 1

    def breed(self, grid, animals):
        if self.age >= 3:
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = self.x+dx, self.y+dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[nx][ny] == AnimalType.EMPTY:
                    grid[nx][ny] = AnimalType.ZEBRA
                    animals.append(Zebra(nx, ny))
                    self.age = 0
                    break

class Lion(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hunger = 0

    def move(self, grid, animals):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        prey, empty = [], []


def print_grid(grid):
    for row in grid:
        print('+' + '---+' * GRID_SIZE)
        print('|' + '|'.join(f' {cell.name[0] if cell != AnimalType.EMPTY else " "} ' for cell in row) + '|')
    print('+' + '---+' * GRID_SIZE)

def main():
    random.seed(time.time())
    grid = [[AnimalType.EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    animals = []

    for _ in range(20):
        while True:
            x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if grid[x][y] == AnimalType.EMPTY:
                grid[x][y] = AnimalType.ZEBRA
                animals.append(Zebra(x, y))
                break

    for _ in range(5):
        while True:
            x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if grid[x][y] == AnimalType.EMPTY:
                grid[x][y] = AnimalType.LION
                animals.append(Lion(x, y))
                break