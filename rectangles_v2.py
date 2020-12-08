import unittest
from points_v2 import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie V2"""

    def __init__(self, x1, y1, x2, y2):
        if not (Point(x1, y1) < Point(x2, y2)):
            raise ValueError("Podano złe wierzchołki")
        self.pt1 = Point(x1, y1) #lewy dolny
        self.pt2 = Point(x2, y2) #prawy górny

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
        M = Rectangle(0,0,1,1)
        M.pt1 = self.pt1 + Point(x,y)
        M.pt2 = self.pt2 + Point(x,y)
        return M
        
    def intersection(self, other):
        """Obliczamy wierzchołki możliwego nakładania się i sprawdzamy, czy może istnieć"""
        LewDoln = Point(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y))
        PrawGorn = Point(min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
        if not (PrawGorn > LewDoln):
            return 0
        else:
            return Rectangle(LewDoln.x,LewDoln.y,PrawGorn.x,PrawGorn.y)
    
    def cover(self,other):
        LewDoln = Point(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y))
        PrawGorn = Point(max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
        return Rectangle(LewDoln.x,LewDoln.y,PrawGorn.x,PrawGorn.y)
        
    def make4(self):
        ct = self.center()
        dX = (self.pt2.x - self.pt1.x)/2
        dY = (self.pt2.y - self.pt1.y)/2
        Rc = Rectangle(ct.x, ct.y, self.pt2.x, self.pt2.y)
        return (Rc, Rc.move(-dX,0),Rc.move(-dX,-dY),Rc.move(0,-dY))
# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    A = Rectangle(2,3,4,7)
    B = Rectangle(-2.5,7,10.55,80)
    C = Rectangle(2,3,4,5)
    
    Q = Rectangle(2,3,6,7)
    W = Rectangle(1,5,3,10)
    E = Rectangle(2,3,3,7)
    R = Rectangle(8,4,14,7)
    T = Rectangle(-8,-4,-4,-1)
    
    


    def test_error(self):      # test raise ValueError
        with self.assertRaises(ValueError): Rectangle(2,7.56,-3,7.56)
        with self.assertRaises(ValueError): Rectangle(2,3,3,3)
        
    def test_print(self):    
        self.assertEqual(str(self.A),'[(2.00, 3.00), (4.00, 7.00)]')
        self.assertEqual(repr(self.A),'Rectangle(2.00,3.00,4.00,7.00)')
        self.assertEqual(str(self.B),'[(-2.50, 7.00), (10.55, 80.00)]')
        self.assertEqual(repr(self.B),'Rectangle(-2.50,7.00,10.55,80.00)')
    
    def test_cmp(self): #Test == != 
        self.assertTrue(self.A == self.A)
        self.assertFalse(self.A == Rectangle(2,-3,4,7))
        
        self.assertTrue(self.B != self.C)
        self.assertTrue(self.B != Rectangle(-2.5,7,10.555,80))
        self.assertFalse(self.B != Rectangle(-2.50,7,10.550,8*10))
    
    def test_ary(self):
        self.assertEqual(self.Q.center(),Point(4,5))
        self.assertEqual(self.W.center(),Point(2,7.5))
        self.assertEqual(self.E.center(),Point(2.50,5))
        self.assertEqual(self.R.center(),Point(11.0, 5.5))
        
        self.assertEqual(self.Q.area(),16)
        self.assertEqual(self.E.area(),4)
        self.assertEqual(self.T.area(),12)
    
    def test_tran(self):
        self.assertEqual(self.Q.move(0,0),Rectangle(2,3,6,7))
        self.assertEqual(self.W.move(1,-1),Rectangle(2,4,4,9))
        self.assertEqual(self.E.move(5,3),Rectangle(7,6,8,10))
        self.assertNotEqual(self.T.move(-1.5,0),Rectangle(-9.5,-4,-5.5,1))
    
    def test_inter(self):
        self.assertEqual(Rectangle.intersection(Rectangle(0,0,2,2),Rectangle(1,1,6,6)),Rectangle(1,1,2,2))
        self.assertEqual(Rectangle.intersection(Rectangle(-1,2,1,4),Rectangle(0,0,5,6)),Rectangle(0,2,1,4))
        self.assertEqual(Rectangle.intersection(Rectangle(0,0,4,7),Rectangle(1,2,3,4)),Rectangle(1,2,3,4))
        self.assertEqual(Rectangle.intersection(Rectangle(0,0,2,2),Rectangle(2,2,6,7)),0)
        self.assertEqual(Rectangle.intersection(Rectangle(0,0,2,2),Rectangle(2,-2,6,3)),0)
        self.assertEqual(Rectangle.intersection(self.A,self.R),0)
        
    def test_cover(self):
        self.assertEqual(Rectangle.cover(Rectangle(0,0,2,2),Rectangle(1,1,6,6)),Rectangle(0,0,6,6))
        self.assertEqual(Rectangle.cover(Rectangle(-1,2,1,4),Rectangle(0,0,5,6)),Rectangle(-1,0,5,6))
        self.assertEqual(Rectangle.cover(Rectangle(0,0,4,7),Rectangle(1,2,3,4)),Rectangle(0,0,4,7))
        self.assertEqual(Rectangle.cover(Rectangle(0,0,10,1),Rectangle(5,-4,6,-2)),Rectangle(0,-4,10,1.00))
        
    def test_make4(self):
        self.assertEqual(Rectangle(0,0,2,2).make4(),(Rectangle(1.00,1.00,2.00,2.00), Rectangle(0.00,1.00,1.00,2.00), Rectangle(0.00,0.00,1.00,1.00), Rectangle(1.00,0.00,2.00,1.00)))
        self.assertEqual(Rectangle(-8,-4,-4,-1).make4(), (Rectangle(-6.00,-2.50,-4.00,-1.00), Rectangle(-8.00,-2.50,-6.00,-1.00), Rectangle(-8.00,-4.00,-6.00,-2.50), Rectangle(-6.00,-4.00,-4.00,-2.50)))



if __name__ == "__main__":
    unittest.main(exit=False)