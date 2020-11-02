#1 kod działa, ale zbędne ; w if'ie (pseudo C/C++)
x=2; y=3
if (y>x):
    result = x
else:
    result = y
print(result)

print('\t')

#2 kod nie działa, warunek if trzeba rozpocząć z wcięciem
for i in 'qwerty' :
    if ord(i) > 100: print(i)
    
print('\t')
    
#3 kod działa, gdyż warunek jest zagnieżdżony w f-ji print
for i in 'asdfgh' : print (ord(i) if ord(i) < 100 else i)