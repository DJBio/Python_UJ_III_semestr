import unittest
from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie"""

    def __init__(self, x1, y1, x2, y2):
        if Point.ComLine(Point(x1, y1),Point(x2, y2)):
            raise ValueError
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({:.2f},{:.2f},{:.2f},{:.2f})".format(self.pt1.x,self.pt1.y, self.pt2.x,self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        D = self.pt2-self.pt1
        return self.pt1 + Point(D.x*0.5,D.y*0.5)

    def area(self):            # pole powierzchni
        D = self.pt2-self.pt1
        return abs(D.x*D.y)
    def move(self, x, y):      # przesunięcie o (x, y) in-place
        self.pt1 = self.pt1 + Point(x,y)
        self.pt2 = self.pt2 + Point(x,y)
        return self

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    A = Rectangle(2,3,4,7)
    B = Rectangle(-2.5,7,10.55,80)
    C = Rectangle(2,3,4,5)
    
    Q = Rectangle(2,3,6,7)
    W = Rectangle(1,5,3,10)
    E = Rectangle(2,3,-3,7)
    R = Rectangle(8,4,4,7)
    T = Rectangle(8,4,-4,-7)


    def test_error(self):      # test raise ValueError
        with self.assertRaises(ValueError): Rectangle(2,7.56,-3,7.56)
        with self.assertRaises(ValueError): Rectangle(2,3,2,7)
        
    def test_print(self):    
        self.assertEqual(str(self.A),'[(2.00, 3.00), (4.00, 7.00)]')
        self.assertEqual(repr(self.A),'Rectangle(2.00,3.00,4.00,7.00)')
        self.assertEqual(str(self.B),'[(-2.50, 7.00), (10.55, 80.00)]')
        self.assertEqual(repr(self.B),'Rectangle(-2.50,7.00,10.55,80.00)')
    
    def test_cmp(self): #Test == != 
        self.assertTrue(self.A == self.A)
        self.assertFalse(self.A == Rectangle(2,3,-4,7))
        
        self.assertTrue(self.B != self.C)
        self.assertTrue(self.B != Rectangle(-2.5,7,10.555,80))
        self.assertFalse(self.B != Rectangle(-2.50,7,10.550,8*10))
    
    def test_ary(self):
        self.assertEqual(self.Q.center(),Point(4,5))
        self.assertEqual(self.W.center(),Point(2,7.5))
        self.assertEqual(self.E.center(),Point(-0.5,5))
        self.assertEqual(self.R.center(),Point(6.00, 5.50))
        
        self.assertEqual(self.Q.area(),16)
        self.assertEqual(self.E.area(),20)
        self.assertEqual(self.T.area(),132)
    
    def test_tran(self):
        self.assertEqual(self.Q.move(0,0),Rectangle(2,3,6,7))
        self.assertEqual(self.W.move(1,-1),Rectangle(2,4,4,9))
        self.assertEqual(self.E.move(5,3),Rectangle(7,6,2,10))
        self.assertNotEqual(self.R.move(-1.5,0),Rectangle(6.50,4.0,-2.5,7.00))


if __name__ == "__main__":
    unittest.main(exit=False)