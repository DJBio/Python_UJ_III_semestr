'''Moduł Pythona z funkcą frequencysort(), która sortuje liczby w tablicy L zgodnie z częstością ich występowania.'''
from random import (shuffle,gauss,randrange)
import matplotlib.pyplot as plt
from Zad_11_1 import *

def frequencysort(L):
    '''Funkcja która sortuje liczby w tablicy L zgodnie z częstością ich występowania'''
    D = {}
    for x in range(0,len(L)):
        if not L[x] in D:
            D[L[x]] = [1,-x]
        else:
            D[L[x]][0] += 1
    L = sorted(L, key = D.get, reverse = True)
    #print(D)
    return L

if __name__ == "__main__":    
    #F = lislos_5(100)
    F = [5,2,2,6,5,7,3,7,3,0,7,2]
    print(F)
    print(frequencysort(F))