digit=2**10000
line = str(digit)
D={}
for i in range(10):
    D[i] = line.count(str(i))

for (liczba, ile) in D.items():
    print('Wystąpienie cyfry - %s wynosi: %s %s' % (liczba, ile, '-'*(ile//10)))