import unittest
import main 
class SquareTest(unittest.TestCase): 
    def test_square_1(self):
        expected = 25
        square = main.Square(5).square()
    def test_square_2(self):
        expected = "Name cannot be lower then 0"
        square = main.Square(-1).square()    
        self.assertEqual(expected, square)
class RectangleTest(unittest.TestCase):
    def test_square_1(self):
        expected = 12
        square = main.Rectangle(3,4).square()
        self.assertEqual(expected, square)
    def test_square_2(self):
        expected = "Name cannot be lower then 0"
        square = main.Rectangle(-1,4).square()
        self.assertEqual(expected, square)    
class CircleTest(unittest.TestCase):    
    def test_square_1(self):
        expected = 314
        square = main.Circle(10).square()
        self.assertEqual(expected,square)
    def test_square_2(self):
        expected = "Name cannot be lower then 0"
        square = main.Circle(-1).square()
        self.assertEqual(expected,square)    
class DimondTest(unittest.TestCase):    
    def test_square_1(self):
        expected = 7.5
        square = main.Dimond(5,3).square()
        self.assertEqual(expected, square)
    def test_square_2(self):
        expected = "Name cannot be lower then 0"
        square = main.Dimond(-5,2).square()
        self.assertEqual(expected, square)
