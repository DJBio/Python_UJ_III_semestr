'''Moduł definiujący działania na łamkach, na końcu przedstawione testy dla tego modułu.
Stosowana jest konwencja, że minus, dla liczb ujemnych, jest tylko i wyłącznie przy liczebniku.
Nie zaimplimentowano sprawdzianu dla położenia minusa, więc warto zwracać uwagę na to samemu!'''

from math import gcd as nwd
import unittest

def add_frac(frac1, frac2):        # frac1 + frac2
    ans = [frac1[0]*frac2[1]+frac1[1]*frac2[0],frac1[1]*frac2[1]]
    faktor = nwd(abs(ans[0]),abs(ans[1]))
    return [int(x/faktor) for x in ans]

def sub_frac(frac1, frac2):         # frac1 - frac2
    ans = [frac1[0]*frac2[1]-frac1[1]*frac2[0],frac1[1]*frac2[1]]
    faktor = nwd(abs(ans[0]),abs(ans[1]))
    return [int(x/faktor) for x in ans]
    
def mul_frac(frac1, frac2):        # frac1 * frac2
    ans = [frac1[0]*frac2[0],frac1[1]*frac2[1]]
    faktor = nwd(abs(ans[0]),abs(ans[1]))
    return [int(x/faktor) for x in ans]
    
def div_frac(frac1, frac2):        # frac1 / frac2
    if (True in [x < 0 for x in frac2]):
        frac2 = [-1*x for x in frac2]
    ans = [frac1[0]*frac2[1],frac1[1]*frac2[0]]
    faktor = nwd(abs(ans[0]),abs(ans[1]))
    return [int(x/faktor) for x in ans]
    
def is_positive(frac):             # bool, czy dodatni
    if frac[0] <= 0:
        return False
    else:
        return True
        
def is_zero(frac):                 # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else:
        return False
    
def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    if frac1[0]/frac1[1] == frac2[0]/frac2[1]:
        return 0
    elif frac1[0]/frac1[1] > frac2[0]/frac2[1]:
        return 1
    else:
        return -1
    
    
def frac2float(frac,dokl=3):              # konwersja do float, dokl - dokładność zaokrąglęnia
    return round(frac[0]/frac[1],dokl)

class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([5, 7], [14, 10]), [74, 35])
        self.assertEqual(add_frac([0, 7], [14, 10]), [7, 5])
        self.assertEqual(add_frac([0, 7], [0, 10]), [0, 1])
        self.assertEqual(add_frac([5, 7], [-6, 10]), [4, 35])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([5, 7], [14, 10]), [-24, 35])
        self.assertEqual(sub_frac([0, 7], [14, 10]), [-7, 5])
        self.assertEqual(sub_frac([0, 7], [0, 10]), [0, 1])
        self.assertEqual(sub_frac([5, 7], [-6, 10]), [46, 35])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([5, 7], [14, 10]), [1, 1])
        self.assertEqual(mul_frac([0, 7], [14, 10]), [0, 1])
        self.assertEqual(mul_frac([0, 7], [0, 10]), [0, 1])
        self.assertEqual(mul_frac([5, 7], [-6, 10]), [-3, 7])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([5, 7], [14, 10]), [25, 49])
        self.assertEqual(div_frac([0, 7], [14, 10]), [0, 1])
        self.assertEqual(div_frac([1, 7], [3, 10]), [10, 21])
        self.assertEqual(div_frac([5, 7], [-6, 10]), [-25, 21])
        self.assertEqual(div_frac([-5, 7], [-6, 10]), [25, 21])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([5, 7]), True)
        self.assertEqual(is_positive([0, 7]), False)
        self.assertEqual(is_positive([1, 7]), True)
        self.assertEqual(is_positive([-5, 7]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([-1, 2]), False)
        self.assertEqual(is_zero([5, 7]), False)
        self.assertEqual(is_zero([0, 7]), True)
        self.assertEqual(is_zero([1, 7]), False)
        self.assertEqual(is_zero([-5, 7]), False)
        self.assertEqual(is_zero([-0, 7]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([-1, 2],[1,-2]), 0) #_1 Owszem, matematycznie to prawda, jednakże wobiec naszej konnwencji jest to błędnie
        self.assertEqual(cmp_frac([5, 7],[12,17]), 1) #_2 poprawnie by było zasygnalizowanie o niemożliwości porównania, a jesczej lepiej
        self.assertEqual(cmp_frac([0, 7],[0,83]), 0)  #_3 byłoby zamiana [1,-2] na [-1,2]
        self.assertEqual(cmp_frac([1, 7],[4,28]), 0)
        self.assertEqual(cmp_frac([-5, 7],[-85,257]), -1)
        self.assertEqual(cmp_frac([-5, 13],[-25,65]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([-1, 2]),-0.5)
        self.assertEqual(frac2float([5, 7]),0.714)
        self.assertEqual(frac2float([0, 7]),0)
        self.assertEqual(frac2float([1, 7],5),0.14286)
        self.assertEqual(frac2float([-5, 7],2),-0.71)
        self.assertEqual(frac2float([523, 17],3),30.765)
    
if __name__ == '__main__':
    unittest.main(exit=False)     # uruchamia wszystkie testy
