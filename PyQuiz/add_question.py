import json
import time
import os
import sys

def top_list():
    with open(os.path.join(sys.path[0],'Pytania','TEMATY.json'), 'r',
            encoding='utf8') as f:
        global TOPICS_LIST
        TOPICS_LIST = json.load(f)
#ta lista ma łączyć nazwy plików JSON z pytaniami => wybór kategorii w test()


def dodanie_pytanie_dziedzina():
    flag = False
    top_list()
    try:
        print("\nWybierz dziedzinę do której chcech dodać pytanie lub [0] dla stworzenia nowej:")
        for x in range(len(TOPICS_LIST)):
            print("({})-> {}".format(x+1,TOPICS_LIST[x]))
        choice = int(input("\nWprowadź numer tematu lub 0:"))
        if choice == 0:
            with open(os.path.join(sys.path[0],'Pytania','TEMATY.json'), 'r+',
                    encoding='utf8') as f:
                TOPICS_LIST.append(input('Wprowadź nazwę nowej dziedziny:\n'))
                json.dump(TOPICS_LIST, f, ensure_ascii=False, indent=1)
            top_list()
        elif choice > len(TOPICS_LIST) or choice < 1:
            print("\nNiepoprawna wartość. Wprowadź od nowa\n")
            flag = True
    except ValueError as e:
        print("\nNiepoprawna wartość. Wprowadź od nowa\n")
        flag = True

    if not flag:
        add_question(os.path.join(sys.path[0],'Pytania',
            TOPICS_LIST[choice-1]+'.json'))
    else:
        dodanie_pytanie_dziedzina()# od nowa jeżeli flaga = True
        


def add_question(filename, pytanie = None, pyt_z_odp = None):
    flag = False
    try:
        if pytanie:
            play = '1'
        else:
            print("Dodać nowe pytanie?\nTak - [Enter]\nNie - [0]")
            play = input()
        if play.lower() not in ['0', 'n', 'nie','t','1','tak','']:
            raise ValueError("Poprawne wartości: Enter/Y or 0/N")
        if play.lower() in ['0', 'n','nie'] :
            return print('\n{:_^80s}\n'.format("DANE ZAPISANO"))
        if not pytanie:
            nowe_pytanie = {}               
            nowe_pytanie = {"pytanie" : input("Proszę o wprowadzenie pytania:\n")}
            nowe_pytanie["odpowiedzi"] = []
        if pytanie and not pyt_z_odp :
            nowe_pytanie = pytanie
        if not pyt_z_odp :
            try:
                ile = int(input("Ile możliwych odpowiedzi?:\n"))
                if ile < 1:
                    raise ValueError
                for x in range (ile):
                    nowe_pytanie["odpowiedzi"].append(input("Proszę o "
                        "wprowadzenie wariantu odpowiedzi:\n{}.".format(x+1)))
            except ValueError as e:
                print("Niepoprawna wartość. Wprowadź naturalną liczbę większą od 0\n")
                return add_question(filename, nowe_pytanie) # zaczyna od razu od miejsca gdzie rzucono ValueError
        else:
            nowe_pytanie = pyt_z_odp
        try:
            popr = int(input("Proszę o wprowadzenie numeru poprawnej odpowiedzi:\n"))
            if popr < 1 or popr > len(nowe_pytanie["odpowiedzi"]):
                raise ValueError
            nowe_pytanie["poprawna_odp"] = popr
        except ValueError as e:
            print("Niepoprawna wartość. Wprowadź naturalną liczbę od 1 do {}\n".format(len(nowe_pytanie["odpowiedzi"])))
            return add_question(filename,True, nowe_pytanie) # zaczyna od razu od miejsca gdzie rzucono ValueError
            
        nowe_pytanie_num = {}
        try:    
            with open(filename, "r+", encoding='utf8') as file:
                if os.stat(filename).st_size == 0:
                    
                    nowe_pytanie_num["Ilość pytań"] = 1
                    nowe_pytanie_num[1] = nowe_pytanie
                    json.dump(nowe_pytanie_num, file, ensure_ascii=False, indent=3)
                    print("Dodano pytanie. Ilość obecnych pytań: 1")
                else:
                    data = json.load(file)
                    
                    nowe_pytanie_num[data["Ilość pytań"]+1] = nowe_pytanie
                    data.update(nowe_pytanie_num)
                    data["Ilość pytań"] += 1
                    file.seek(0)
                    json.dump(data, file, ensure_ascii=False, indent=3)
                    print("Dodano pytanie.Ilość obecnych pytań: {}".format(data["Ilość pytań"]))
        except IOError:
            with open(filename, "w+", encoding='utf8') as file:
                if os.stat(filename).st_size == 0:                 
                    nowe_pytanie_num["Ilość pytań"] = 1
                    nowe_pytanie_num[1] = nowe_pytanie
                    json.dump(nowe_pytanie_num, file, ensure_ascii=False, indent=3)
                    print("Dodano pytanie. Ilość obecnych pytań: 1")
                else:                    
                    raise ValueError("Dziwne, tak nie powinno być")
        
        return (add_question(filename))
    
    except:
        print("\nNiepoprawna wartość. Wprowadź od nowa \n{}\n".format(sys.exc_info()[1]))
        add_question(filename)
        
if __name__ == '__main__':

    dodanie_pytanie_dziedzina()
