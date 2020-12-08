from math import sqrt
def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    h = 0.5*(a+b+c)
    if h - max(a,b,c) < 0 or any( x <= 0 for x in (a, b, c)):
        raise ValueError("Trójkąt o takich bokach nie istnieje w przestrzeni euklidesowej")
    else:
        return sqrt(h*(h-a)*(h-b)*(h-c))

try:
    print(heron(10,5,8))
    print(heron(4,5,3))
    print(heron(10,5,3))
except ValueError as X:
    print(X)