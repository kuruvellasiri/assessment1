from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return "Circle"



class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return "Rectangle"

    


shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:
    print(f"{shape}: area={shape.area()}, perimeter={shape.perimeter()}")
    try:
        Shape()
    except TypeError:
        print("Error: Cannot instantiate abstract class Shape")