from .base import Shape

class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def compute_area(self):
        return 0.5 * self.base * self.height

    def compute_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def __str__(self):
        return (
            f"Triangle:\n"
            f"  Base: {self.base}\n"
            f"  Height: {self.height}\n"
            f"  Sides: {self.side_a}, {self.side_b}, {self.side_c}\n"
            f"  Area: {self.compute_area()}\n"
            f"  Perimeter: {self.compute_perimeter()}"
        )
