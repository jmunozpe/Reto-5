# ======================================================
# el paquete con módulos separados (shapes/)
# ======================================================

from shapes import Rectangle, Circle, Triangle

print("=== Ejecución usando paquete shapes/ ===\n")

rect = Rectangle(4, 6)
circle = Circle(3)
tri = Triangle(base=4, height=3, side_a=3, side_b=4, side_c=5)

print(rect)
print()
print(circle)
print()
print(tri)

# ======================================================
# el paquete con módulo único (module_shapes/)
# ======================================================

from module_shapes.shapes import Rectangle as ModRectangle, Circle as ModCircle, Triangle as ModTriangle

print("\n\n=== Ejecución usando paquete module_shapes/ ===\n")

rect2 = ModRectangle(5, 7)
circle2 = ModCircle(3)
tri2 = ModTriangle(base=4, height=3, side_a=3, side_b=4, side_c=5)

print(rect2)
print()
print(circle2)
print()
print(tri2)
