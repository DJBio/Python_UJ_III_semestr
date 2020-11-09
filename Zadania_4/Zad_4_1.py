X = "qwerty"

def func():
    global X
    X = 5
    print (X)
    
print (X)
func()
print(X)
