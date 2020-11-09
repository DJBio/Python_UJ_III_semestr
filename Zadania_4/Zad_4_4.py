def fab_it(n):
    if  n in (0,1):
        return n
    else:
        L1 = 1
        L2 = 1
        for i in range(2,n):
            L1,L2 = L2,L2+L1
        return L2
print(fab_it(1))
print(fab_it(2))
print(fab_it(3))
print(fab_it(4))
print(fab_it(5))
print(fab_it(6))
print(fab_it(7))
print(fab_it(8))
print(fab_it(9))
print(fab_it(10))