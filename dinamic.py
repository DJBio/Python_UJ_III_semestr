import timeit
def din_fun(i, j):
    """Funkcja zwrócająca wartość f-ji P(i, j), zdefiniowana w zad. 8.6"""
    if any(x < 0 for x in (i,j)): raise ValueError
    if any(x == 0 for x in (i,j)):
        if j != 0:
            return 1.0
        elif i != 0:
            return 0.0
        else:
            return 0.5
    Table = {}
    Table['0'] = {0.5}
    for x in range(1,i+1):
        Table[str(x)+',0'] = 0
    for x in range(1,j+1):
        Table['0,'+str(x)] = 1

    for x in range(1,i+1):
        for y in range(1,j+1):
            Table[str(x)+','+str(y)] = 0.5*(Table[str(x-1)+','+str(y)] + Table[str(x)+','+str(y-1)])
    return Table[str(i)+','+str(j)]
    
def rek_fun(i, j):
    """Funkcja zwrócająca wartość f-ji P(i, j), zdefiniowana w zad. 8.6. Rekurencyjna"""
    if any(x < 0 for x in (i,j)): raise ValueError
    if any(x == 0 for x in (i,j)):
        if j != 0:
            return 1.0
        elif i != 0:
            return 0.0
        else:
            return 0.5
    return 0.5*(rek_fun(i-1,j)+rek_fun(i,j-1))
    
mysetup = '''
from __main__ import (din_fun,rek_fun)
'''
    
print ("Czas rekurencyjnego algorytmu:",timeit.timeit(setup = mysetup, 
                                                     stmt = '''rek_fun(7,7)''', 
                                                     number = 1000))
print ("Czas dynamicznego algorytmu:", timeit.timeit(setup = mysetup, 
                                                     stmt = '''din_fun(7,7)''', 
                                                     number = 1000))