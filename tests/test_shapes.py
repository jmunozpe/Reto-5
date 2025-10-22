from shapes import Rectangle, Circle, Triangle
import math

def test_rectangle():
    r = Rectangle(4, 6)
    assert r.compute_area() == 24
    assert r.compute_perimeter() == 20

def test_circle():
    c = Circle(3)
    assert math.isclose(c.compute_area(), math.pi * 9, rel_tol=1e-9)
    assert math.isclose(c.compute_perimeter(), 2 * math.pi * 3, rel_tol=1e-9)

def test_triangle():
    t = Triangle(base=4, height=3, side_a=3, side_b=4, side_c=5)
    assert t.compute_area() == 6.0
    assert t.compute_perimeter() == 12
