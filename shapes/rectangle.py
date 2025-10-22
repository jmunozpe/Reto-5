from .base import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return (
            f"Rectangle:\n"
            f"  Width: {self.width}\n"
            f"  Height: {self.height}\n"
            f"  Area: {self.compute_area()}\n"
            f"  Perimeter: {self.compute_perimeter()}"
        )

