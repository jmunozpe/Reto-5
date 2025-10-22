from shapes import Rectangle, Circle, Triangle

def mostrar(figura):
    nombre = type(figura).__name__
    print(f"{nombre} -> área = {figura.area():.2f}, perímetro = {figura.perimeter():.2f}")

if __name__ == "__main__":
    r = Rectangle(3, 4)
    c = Circle(2)
    t = Triangle(a=3, b=4, c=5, base=4, height=2.5)

    mostrar(r)
    mostrar(c)
    mostrar(t)
