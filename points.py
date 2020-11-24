"""Moduł definiujący klasę Point"""
class Point:
    """Klasa reprezentująca punkt (x,y)"""
    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return "({:.2f}, {:.2f})".format(self.x, self.y)

    def __repr__(self):             # zwraca string "Point(x, y)"
        return "Punkt({:.2f}, {:.2f})".format(self.x, self.y)

    def __eq__(self, other):        # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)
    
    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other
    
    def ComLine(self, other):
        return (self.x == other.x) or (self.y == other.y) #sprawdzenie, czy leżą na jednej prostej
        
    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return (self.x**2+self.y**2)**0.5

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points


# Kod testujący moduł

import unittest

class TestPoint(unittest.TestCase):
    
   
    A = Point(2,1.8)
    B = Point(2,7)
    C = Point(5.5,7)
    D = Point(5.5,1.8)
    F = Point(-10,56.8)
    P = Point(3,4)
    
    def test_print(self):      # test str() i repr()
        self.assertEqual(str(Point(2,6)),'(2.00,6.00)')
        self.assertEqual(repr(Point(2,6)),'Punkt(2.00,6.00)')
        self.assertEqual(str(Point(2.79526,-10.9825)),'(2.80,-10.98)')
        self.assertEqual(repr(Point(2.79426,-10.9825)),'Punkt(2.79,-10.98)')

    def test_cmp(self): #Test == != ComLine
        self.assertTrue(Point(2,6) == Point(2.0,6.0))
        self.assertFalse(Point(-2,6) == Point(2.0,6.0))
        
        self.assertTrue(Point(-2,6) != Point(2.0,6.0))
        self.assertTrue(Point(3,10.8) != Point(10.8,3))
        self.assertFalse(Point(2,6) != Point(2.0,6.0))
        
        self.assertTrue(Point.ComLine(self.A,self.B))
        self.assertFalse(Point.ComLine(self.A,self.C))
        self.assertTrue(Point.ComLine(self.A,self.D))
        
    def test_ary(self):   #Test + - * x
        self.assertEqual(self.A+self.B,Point(4,8.8))
        self.assertEqual(self.B+self.F,Point(-8,63.8))
        self.assertEqual(self.C-self.B,Point(3.5,0))
        self.assertEqual(self.D-self.F,Point(15.5,-55))
        
        self.assertEqual(Point.length(self.A),(2**2+1.8**2)**0.5)
        self.assertEqual(Point.length(self.P),5)
        
        self.assertEqual(self.B*self.D, 23.6)
        self.assertEqual(self.C*self.P, 44.5)
        
        self.assertEqual(Point.cross(self.B,self.F), 183.6)
        self.assertEqual(Point.cross(self.C,self.P), 1)

    def test_hash(self):
        self.assertEqual(hash(self.F),hash((-10,56.8)))
        self.assertEqual(hash(self.B),hash((2,7)))


if __name__ == "__main__":
    unittest.main(exit=False)     # wszystkie testy