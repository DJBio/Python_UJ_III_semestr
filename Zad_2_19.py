L=[1,6,7,23,45,78,125,478,63,12,45,4]
L.sort()
for i in range(len(L)):
    a=str(L[i])
    L[i] = a.zfill(3)

napis = "_".join(str(x) for x in L)
print(napis)