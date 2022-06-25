from abc import ABC
from abc import abstractclassmethod
import math
class Figure(ABC):
    @abstractclassmethod
    def __init__(self):
        pass
    @abstractclassmethod
    def square(self, *args):
        pass
class Square(Figure):
    def __init__(self, a):
        self.a = a
    def square(self):
        if self.a<0:
            return None
        return self.a **2
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def square(self):
        if self.a<0 or self.b<0:
            return None
        return self.a * self.b    
class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def square(self):
        if self.r<0:
            return None
        return self.r **2 * math.pi
class Dimond(Figure):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    def square(self):
        if self.d1<0 or self.d2<0:
            return None
        return  self.d1*self.d2*0.5
