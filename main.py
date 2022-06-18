from abc import ABC
from abc import abstractclassmethod
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
        return self.a **2
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def square(self):
        return self.a * self.b    
class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def square(self):
        return self.r **2 * 3.14
class Dimond(Figure):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    def square(self):
        return  self.d1*self.d2*0.5

