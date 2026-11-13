class Circle:
    def area(self):
        return "THIS IS CIRCLE"

class Rectangle:
    def area(self):
        return "THIS IS RECTANGLE"

class Triangle:
    def area(self):
        return "THIS IS TRIANGLE"

def print_area(shape):
    print(shape.area())

c = Circle()
r = Rectangle()
t = Triangle()
print_area(c)
print_area(r)
print_area(t)

