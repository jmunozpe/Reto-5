from math import pi

class Shape:
    def compute_area(self):
        raise NotImplementedError("Debes implementar este método en la subclase.")

    def compute_perimeter(self):
        raise NotImplementedError("Debes implementar este método en la subclase.")


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

