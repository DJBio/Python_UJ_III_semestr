def factorial_it(n):
    if  n == 1 or n == 1:
        return 1
    else:
        L = 1
        for i in range(2,n+1):
            L = L*i
        return L
print(factorial_it(1))
print(factorial_it(2))
print(factorial_it(3))
print(factorial_it(4))
print(factorial_it(10))
print(factorial_it(110))
print(factorial_it(109))
