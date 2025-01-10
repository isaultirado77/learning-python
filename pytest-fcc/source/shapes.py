import math
from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod
    def area(self) -> float: 
        pass

    @abstractmethod
    def perimeter(self) -> float: 
        pass

class Circle(Shape):
    def __init__(self, r: float):
        self.radius = r

    def area(self): 
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.l = length
        self.w = width

    def area(self) -> float:
        return self.l * self.w

    def perimeter(self) -> float:
        return 2.0 * self.l + 2.0 * self.w

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle): 
            return False
        return self.w == other.w and self.l == other.l

