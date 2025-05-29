class AnimalType(Enum):
    EMPTY:0
    ZEBRA:1
    LION:2

class Animal:
    def __init__(self, x:int, y:int):
        self.x=x
        self.y=y