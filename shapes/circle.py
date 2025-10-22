from math import pi
from .base import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return (
            f"Circle:\n"
            f"  Radius: {self.radius}\n"
            f"  Area: {self.compute_area():.2f}\n"
            f"  Circumference: {self.compute_perimeter():.2f}"
        )

