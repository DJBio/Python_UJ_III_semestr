print('Cześć użytkowniku')

try:
    x = int(input('Proszę o podanie długości suwmiarki\n'))
    start = '|'
    unit = '....|'
    miarka = start + unit*x + '\n' + '0'

    for i in range (1,x+1):
        miarka = miarka + str(i).rjust(5)

    print(miarka)
except ValueError:
    print("Proszę o podanie liczby całkowitej\n")



