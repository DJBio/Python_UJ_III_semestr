'''Moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania'''
from random import (shuffle,gauss,randrange)
import matplotlib.pyplot as plt 

def lislos_1(N):
    '''Funkcja tworząca listę liczb całkowitych od 0 do N-1 w kolejności losowej'''
    D=[x for x in range (N)]
    shuffle(D)
    return D
    
def lislos_2(N,krok = 10):
    '''Funkcja tworząca listę liczb całkowitych od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji).
       Parametr 'krok' określa jak dokładnie jest posortowana tablica (coś w stylu szerokości rozrzutu, ale nie do końca). Jeżeli krok >= N, to działa jak lislos_1'''
    ile = N//krok
    D=[]
    for i in range(1,ile+1):
        d = [x for x in range((i-1)*krok,i*krok)]
        shuffle(d)
        D += d
    d = [x for x in range(ile*krok,N)]
    shuffle(d)
    D += d
    return D

def lislos_3(N,krok = 10):
    '''Funkcja tworząca odwrotną listę liczb całkowitych od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji).
       Parametr 'krok' określa jak dokładnie jest posortowana tablica (coś w stylu szerokości rozrzutu, ale nie do końca). Jeżeli krok >= N, to działa jak lislos_1, tylko odwrotnie'''
    D = lislos_2(N, krok)
    D.reverse()
    return D

def lislos_4(N,szer = 1):
    '''Funkcja tworząca listę liczb N liczb float w kolejności losowej o rozkładzie gaussowskim. szer to SD. wartość średnia -> 0'''
    D=[gauss(0,szer) for x in range (N)]
    return D

def lislos_5(N):
    '''Funkcja tworząca listę N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N)'''
    D = []
    while N:
        i = randrange(N+10)
        ile = randrange(1,N//10+2)
        D += [i]*ile
        N -= ile
    shuffle(D)
    return D
