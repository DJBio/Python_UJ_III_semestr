rym2int = {'M':'1000','D':'500','C':'100','L':'50','X':'10','V':'5','I':'1'}
rym2int['CM'] = '900'
rym2int['CD'] = '400'
rym2int['XC'] = '90'
rym2int['XL'] = '40'
rym2int['IX'] = '9'
rym2int['IV'] = '4'

while (True):
    rzym = input('Proszę o podanie liczby rzymskiej. "Stop", żeby skończyć\n').upper()
    if (rzym == 'STOP'):
        print("Do zobaczenia"); break
    
    try:
        cyfry = []
        i = 0
        while i < len(rzym):
            if (i+1 <= len(rzym)-1) and int(rym2int[ rzym[i+1] ]) > int(rym2int[ rzym[i] ]):
                cyfry.append( int(rym2int[ rzym[i] + rzym[i+1] ] ))
                i+=2
            else:
                cyfry.append( int(rym2int[ rzym[i] ] ))
                i+=1

        
        liczba = sum(cyfry)
        print(liczba)
    except KeyError:
        print("Ojejku, to nie liczba rzymska\n")
    