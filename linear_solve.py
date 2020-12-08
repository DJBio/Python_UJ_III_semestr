
def solve(a, b, c ):
    """Funkcja rozwiązująca równanie postaci a*x + b*y + c = 0"""
    if a == b == 0:
        if c == 0:
            return "Rozwiązania: (x, y) to dowolna para liczb"
        else:
            return "Brak rozwiązań. Sprzeczność."
    
    if b != 0 and a == 0:
        return "Rozwiązania: (x, {}), x należy do R".format(-c/b)
        
    if a != 0 and b == 0:
        return "Rozwiązania: ({}, y), y należy do R".format(-c/a)
        
    if a != 0 and b != 0:
        if c == 0:
            return "Rozwiązania: (x, {}*x ), x należy do R".format(-a/b)
        else:
            return "Rozwiązania: (x, {}*x{:+}), x należy do R".format(-a/b, -c/b)
        
print(solve(0,0,0))
print(solve(0,0,5))

print(solve(0,3,0))
print(solve(0,5,-9))

print(solve(10,0,0))
print(solve(10,0,-9))

print(solve(10,10,-5))
print(solve(-10,10,5.125))
print(solve(5,-25,0))
    
