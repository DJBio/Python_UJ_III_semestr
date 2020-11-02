print('Cześć użytkowniku. Zaczniemy przygodę ?')
while (True):
    x = input('Proszę o podanie liczby\n')
    if (x == 'stop' or x == 'Stop'):
        print("Do zobaczenia"); break
    
    try:
        x = float(x)
    except ValueError:
        print("Broń Boże! To nie liczba, spróbuj jeszcze raz\n");continue
    
    print('{0:.3f}, {0:.3f}\n{1:.3f}\n'.format(x,x**3))