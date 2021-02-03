from math import ceil
while True:
    start_raw = input ("Podaj początkową stonę; [Enter] => 1\n")
    if start_raw == '':
        start = 1
    else:
        start = int(start_raw)

    stop = int(input ("Podaj końcową stronę\n"))
    ile_raw = input ("Podaj ilość stron na stronicę arkuszu; [Enter] => 4\n")
    if ile_raw == '':
        ile = 4
    else:
        ile = int(ile_raw)
    
    L = list(range(start,stop+1))
    I = []
    II = []
    licznik = 1
    for x in L:
        if licznik <= ile:
            I.append(x)
            licznik += 1
        elif licznik < 2*ile:
            II.append(x)
            licznik += 1
        else:
            II.append(x)
            licznik = 1
    print('I: {}-Liczba arkuszy:{}'.format(I, ceil (len(I)/ile)))
    print('II:{}-Liczba arkuszy:{}\n'.format(II, ceil (len(II)/ile)))
    if ceil (len(I)/ile) != ceil (len(II)/ile):
        print('UWAGA na ostatnim arkuszu będzie wydrukowano:_{} STRON_ z {} możliwych \n\n'.format(len(I)-len(II),2*ile))