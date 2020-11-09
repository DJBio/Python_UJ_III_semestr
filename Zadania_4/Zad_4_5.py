L = list(range(1,16))

def odwr_it(L,lw,pr):
    K = L[:]
    if pr < lw:
        raise ValueError1
    if pr > len(K)-1 :
        raise ValueError
    for i in range(0,int(0.5*(pr-lw)+1)): # wyrażenie int(0.5*(pr-lw)+1) działa jako sufit, określa liczbę zamian + 1
        K[pr-i],K[lw+i] = K[lw+i],K[pr-i]
    return K
    
def odwr_rek(L,lw,pr):
    K = L[:]
    if pr > len(K)-1:
        raise ValueError2
    if lw >= pr:
        return K
    else:
        K[pr],K[lw] = K[lw],K[pr]
        return odwr_rek(K,lw+1,pr-1)
try: 
    L_i = list (odwr_it(L,0,9))
    print(L_i)    
    
    L_r = odwr_rek(L,0,9)
    print(L_r)

except ValueError:
    print("Błąd, nie można odwrócić listy\n")       