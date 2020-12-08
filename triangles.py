import unittest
from points_v2 import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie"""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        Wektor12 = Point(x1, y1) - Point(x2, y2)
        Wektor13 = Point(x1, y1) - Point(x3, y3)
        if (Wektor12.x*Wektor13.y - Wektor12.y*Wektor13.x) == 0 :
            raise ValueError("Podano współliniowe punkty")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[{}, {}, {}]".format(self.pt1, self.pt2, self.pt3)

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):   # obsługa tr1 == tr2, może być różna kolejność, ale położenie w przestrzeni takie same
        return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca centroid trójkąta
        return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3, (self.pt1.y+self.pt2.y+self.pt3.y)/3)

    def area(self):            # pole powierzchni
        return abs(0.5*(self.pt1.x*(self.pt2.y - self.pt3.y) + self.pt2.x*(self.pt3.y - self.pt1.y) + self.pt3.x*(self.pt1.y - self.pt2.y)))

    def move(self, x, y):      # przesunięcie o (x, y) in-place
        M = Triangle(0,0,1,1,0,2)
        M.pt1 = self.pt1 + Point(x,y)
        M.pt2 = self.pt2 + Point(x,y)
        M.pt3 = self.pt3 + Point(x,y)
        return M

    def make4(self):
        pnb12 = Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2) # pnb - punkt na boku na punktach pt1, pt2
        pnb13 = Point((self.pt1.x+self.pt3.x)/2, (self.pt1.y+self.pt3.y)/2)
        pnb32 = Point((self.pt3.x+self.pt2.x)/2, (self.pt3.y+self.pt2.y)/2)
        Trg1 = Triangle(self.pt1.x, self.pt1.y, pnb12.x, pnb12.y, pnb13.x, pnb13.y)
        return (Trg1, Trg1.move(pnb12.x, pnb12.y), Trg1.move(pnb13.x, pnb13.y), Triangle(pnb32.x, pnb32.y, pnb12.x, pnb12.y, pnb13.x, pnb13.y))
# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    A = Triangle(0,0,0,6,4,0)
    B = Triangle(0,0,0,6,4,2)
    C = Triangle(-4,0,4,0,0,4)
    
    def test_error(self):      # test raise ValueError
        with self.assertRaises(ValueError): Triangle(0,0,1,1,7,7)
        
    def test_print(self):    
        self.assertEqual(str(self.A),'[(0.00, 0.00), (0.00, 6.00), (4.00, 0.00)]')
        self.assertEqual(repr(self.A),'Triangle(0.00, 0.00, 0.00, 6.00, 4.00, 0.00)')
    
    def test_cmp(self): #Test == != 
        self.assertTrue(self.A == self.A)
        self.assertTrue(self.A == Triangle(0,6,0,0,4,0))
        self.assertTrue(self.A == Triangle(0,6,4,0,0,0))
        self.assertFalse(self.A == Triangle(0,6,0,0,1,0))
        
        self.assertTrue(self.C == Triangle(-4,0,0,4,4,0))
        self.assertTrue(self.C == Triangle(4,0,-4,0,0,4))
        self.assertTrue(self.C == Triangle(4,0,0,4,-4,0))
        
        self.assertTrue(self.B != self.C)
    
    def test_ary(self):
        self.assertEqual(self.A.center(),Point(4/3,2))
        self.assertEqual(self.B.center(),Point(4/3,8/3))
        
        self.assertEqual(self.A.area(),12)
        self.assertEqual(Triangle(0,6,0,0,4,0).area(),12)
        self.assertEqual(Triangle(0,6,4,0,0,0).area(),12)
        self.assertEqual(self.B.area(),12)
        self.assertEqual(self.C.area(),16)
        self.assertEqual(Triangle(4,0,0,4,-4,0).area(),16)
        self.assertEqual(Triangle(-4,0,0,4,4,0).area(),16)
        
    def test_move(self):
        self.assertEqual(self.A.move(1,5), Triangle(1, 5.00, 1, 11.0, 5.00, 5))
        
    def test_make4(self):
        Wyn = (Triangle(0, 0, 0.00, 3, 2.00, 0), Triangle(0.00, 3, 0.00, 6, 2.00, 3.00), Triangle(2.00, 0, 2.00, 3, 4.00, 0.00), 
        Triangle(2, 3, 0, 3, 2.00, 0))
        
        self.assertEqual(self.A.make4(), Wyn)


if __name__ == "__main__":
    unittest.main(exit=False)