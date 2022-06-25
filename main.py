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
        if a<0:
            raise ValueError("Name cannot be lower then 0")
        else:    
            self.a = a
    def square(self):
        return self.a **2
class Rectangle(Figure):
    def __init__(self, a, b):
        if a<0 or b<0:
            raise ValueError("Name cannot be lower then 0")
        else: 
             self.a = a
             self.b = b
    def square(self):
        return self.a * self.b    
class Circle(Figure):
    def __init__(self, r):
         if r<0:
            raise ValueError("Name cannot be lower then 0")
         else:
           self.r = r
    def square(self):
        return self.r **2 * math.pi
class Dimond(Figure):
    def __init__(self, d1, d2):
         if d1<0 or d2<0:
            raise ValueError("Name cannot be lower then 0")
         else:    
             self.d1 = d1
             self.d2 = d2
    def square(self):
        return  self.d1*self.d2*0.5
