'''Moduł który zawiera dwie funkcji rekurencyjne: factorial oraz fibonacci'''
def factorial(n):
    if n < 0:
        return ValueError
    elif  n in (0,1):
        return 1
    else:
        return n*factorial(n-1)
def fibonacci(n):
    if n < 0:
        return ValueError
    elif  n in (0,1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
