
from random import random
from math import (sqrt, pi)

def calc_pi(ile_prob):
    """Funkcja wyliczająca liczbę pi metodą Monte Carlo"""
    wewn = 0
    for x in range(ile_prob):
        if sqrt(random()**2 + random()**2) <= 1:
            wewn +=1    
    oszac = 4*(wewn/ile_prob)
    return "Oszacowanie pi:{:.5f}. Błąd: {:.3f}%".format(oszac, abs((oszac/pi)-1)*100)

while True:
  print(calc_pi(int(input("Wpisz ilość rzutów\n"))))