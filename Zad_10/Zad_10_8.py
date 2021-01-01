import timeit
from Zad_10_8_v2 import RandomQueue_2
from random import randrange
class RandomQueue:
    '''Kolejka losowa oparta na dynamicznej liście Python'''
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):   # zwraca losowy element
        return self.items.pop(randrange(len(self.items))) #mysłałem nad rozwiązaniem O(const), ale dla implementacji opartej na listach
                                                            #to chyba nie jest możliwe
    def is_empty(self):
        return not self.items

    def is_full(self):
        return False          # W tej implementacji to nie jest możliwe

    def clear(self):     # czyszczenie listy
        del self.items[:]
        return self


mysetup = '''
from __main__ import (RandomQueue)
from Zad_10_8_v2 import RandomQueue_2
pq_1 = RandomQueue()
pq_2 = RandomQueue_2()
'''
mycode_1 = '''
for item in range(1000):
    pq_1.insert(item) 
while not pq_1.is_empty():
    pq_1.remove()
'''
mycode_2 = '''
for item in range(1000):
    pq_2.insert(item) 
while not pq_2.is_empty():
    pq_2.remove()
'''
    
print ("Czas działania kolejki losowej opartej na dynamicznej liście Python:",timeit.timeit(setup = mysetup, stmt = mycode_1, number = 500))# 0,4s (a więc, im mniej kodu, tym szybciej program)
print ("Czas działania kolejki losowej opartej na liście jednokierunkowej:", timeit.timeit(setup = mysetup, stmt = mycode_2, number = 500))#7,5 s


