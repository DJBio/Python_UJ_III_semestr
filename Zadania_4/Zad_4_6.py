L = [1,[(2,[3],[4,(5,[6])]),7,(8,9)],[]]

def suma_totalna(D):
    suma = 0
    for x in range(len(D)):
        if isinstance(D[x],(list,tuple)):
            suma = suma + suma_totalna(D[x])
        else:
            suma = suma + D[x]
    return suma
print (suma_totalna(L))