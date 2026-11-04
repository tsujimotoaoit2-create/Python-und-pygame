import math

class Cuboid:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    def volume(self):
        return self.width * self.height * self.depth
    def surface_area(self):
        return 2 * (
            self.width * self.height
            + self.height * self.depth
            + self.depth * self.width
        )
    def diagonal(self):
        return math.sqrt(self.width**2 + self.height**2 + self.depth**2)

shape1 = Cuboid(width=6, height=4, depth=5)
assert shape1.volume() == 120
assert shape1.surface_area() == 148
assert shape1.diagonal() == math.sqrt(77)

shape2 = Cuboid(width=3, height=3, depth=2)
assert shape2.volume() == 18
assert shape2.surface_area() == 42
assert shape2.diagonal() == math.sqrt(22)