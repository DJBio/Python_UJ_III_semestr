L = [1,[(2,[3],[4,(5,[6])]),[],7,(8,9)]]

def wygladz(D):
    New = []
    for x in range(len(D)):
        if isinstance(D[x],(list,tuple)):
            return New + wygladz(D[x]) + wygladz (D[x+1:])
        else:
            New.append(D[x])
    return New
print (wygladz(L))