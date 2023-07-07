import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius**2
        return round(area, 2)

    def perimeter(self):
        perimeter = self.radius * 2 * math.pi
        return round(perimeter, 2)


circle1 = Circle(radius=1)
circle3 = Circle(radius=3)

print(circle1.area())
print(circle1.perimeter())
print(circle3.area())
print(circle3.perimeter())
