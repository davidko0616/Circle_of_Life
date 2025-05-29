import random

class Zebra(Animal):
    def movement():
        directions = [(-1,0),(1,0)(0,-1),(0,1)]
        dx, dy = random.choice(directions)
        self_x = zebra_x + dx
        self_y = zebra_y + dy
        self.age+=1

    def breed():
        if self.age >= 3:
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            dx, dy = random.choice(directions)
            new_x = self.x + dx
            new_y = self.y + dy
            return Zebra(new_x, new_y, name=self.name + "_clone")