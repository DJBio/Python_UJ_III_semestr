import json
import time
import os
import sys
from tabulate import tabulate
import Add_question as aq

""" Test z biochemii"""
aq.top_list()
#ta lista ma łączyć nazwy plików JSON z pytaniami z możliwością wyboru kategorii w test()

class BioQuiz:
    pass
def zapytaj(dane, flag = True):
    if flag:
        print(tabulate([[x] for x in dane["odpowiedzi"]], headers = ['#',dane["pytanie"]], tablefmt="fancy_grid",showindex=range(1,len(dane["odpowiedzi"])+1)))
        #print(dane['pytanie'])
        #for x in range(len(dane['odpowiedzi'])):
        #    print(dane['odpowiedzi'][x])
    
    try:
        choice = int(input("Wpisz swoją odpowiedź: "))
        if choice < 1 or choice > len(dane["odpowiedzi"]):
            raise ValueError
    except:
        print("Niepoprawna wartość. Wprowadź naturalną liczbę od 1 do {}\n".format(len(dane["odpowiedzi"])))
        return zapytaj(dane, flag = False)# zaczyna od razu od miejsca gdzie rzucono Error
    
    if choice == dane['poprawna_odp']:
        return 2
    else:
        return -1

def test(questions):
    score = 0
    print("\nKrótkie wprowadzenie:\n1. Wprowadzaj tylko symnbol (A/a/1) odpowiadający poprawnej odpowiedzi.\n2. Poprawna odpowiedź daje 2 pkt.\n3. Za złą odpowiedź dostajesz -1\nTest zaraz się zacznie. Powodzenia!")
    time.sleep(5)
    for key, meta in questions.items():
        if key in ("Ilość pytań",):
            continue
        else:
            print("\nPytanie {}:".format(key))
            score += zapytaj(meta)
    print("\n_____________________WYNIK_____________________\n")
    print('Twój wynik: ', score)

def load_question(filename):
    """
    Wczytuje pytania z wybranego pliku JSON 
    """
    qs = None
    with open(filename, "r", encoding='utf8') as read_file:
        qs = json.load(read_file)
    return (qs)


def play_quiz():
    flag = 1
    try:
        print("\nWitam młody biochemiku!\n\nWybierz dziedzinę pytań:")
        for x in range(len(aq.TOPICS_LIST)):
            print("({})-> {}".format(x+1,aq.TOPICS_LIST[x]))
        print("Dodać pytanie -> +")
        choice = input("Wprowadź numer tematu:")
        if choice == '+':
            aq.dodanie_pytanie_dziedzina()
            flag = 0
        else:
            choice = int(choice)
            if choice > len(aq.TOPICS_LIST) or choice < 1:
                print("Niepoprawna wartość. Wprowadź od nowa")
                flag = -1
    except ValueError as e:
        print("Niepoprawna wartość. Wprowadź od nowa")
        flag = -1

    if flag == 1:
        test(load_question(os.path.join(sys.path[0],'Pytania',aq.TOPICS_LIST[choice-1]+'.json')))
    elif flag == -1:
        play_quiz() # od nowa jeżeli flaga = True
    elif flag == 0:
        user_begin_prompt()

def user_begin_prompt():
    print("Chcesz sprawdzić swoją wiedzę z biochemii?\nA. Tak\nB. Nie")
    play = input()
    if play.lower() in ['a', 't', 'tak'] :
        play_quiz()
    elif play.lower() in ['b', 'n','nie']:
        print("Zapraszam ponownie")
    else:
        print("\nNie rozumiem, chyba literówka.\nNaciśnij A aby zagrać, czy B aby wyjść.\n")
        user_begin_prompt()
        

if __name__ == '__main__':

    user_begin_prompt()
