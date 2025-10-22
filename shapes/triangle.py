from .base import Shape

class Triangle(Shape):
    def __init__(self, a, b, c, base, height):
        self.a = a
        self.b = b
        self.c = c
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.a + self.b + self.c
