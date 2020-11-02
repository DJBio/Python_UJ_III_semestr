#lisr.sort działa odrazu na obiekcie, ale nie zwraca go, więc zbędne przepisywanie L = L.sort()
L = [3,5,4]; L.sort();print (L)

# x,y = 1,2,3 - too many values to unpack

x = 1,2,3 ;#x[1] = 4 nie można zmieniać wartości w krotkach

X = [1,2,3];# X[3] = 4; przepisanie poza zasięg 

K = 'abc'; # K.append('b') nie można zmieniać sekwencji

W = list(map(lambda a,b:pow(a,b),L,range(2,10,2))); print(W) #w tym przypadku należało skorzystać z zapisu przez lamdba
