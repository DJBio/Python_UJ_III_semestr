import json
import time
import os
import sys
from tabulate import tabulate
import add_question as aq


aq.top_list()#tworzy globalną listę tematów

class AskModule:
    def __init__(self, name):
        self.name = name
        self.score = 0
        print("\nWitam {}!\n\nWybierz dziedzinę pytań:".format(name))
        self.play_quiz()

    @staticmethod
    def zapytaj(dane, flag = True):
        if flag:
            print(tabulate([[x] for x in dane["odpowiedzi"]],
                headers = ['#',dane["pytanie"]],tablefmt="fancy_grid",
                showindex=range(1,len(dane["odpowiedzi"])+1)))
            #print(dane['pytanie'])
            #for x in range(len(dane['odpowiedzi'])):
            #    print(dane['odpowiedzi'][x])
        
        try:
            choice = int(input("Wpisz swoją odpowiedź: "))
            if choice < 1 or choice > len(dane["odpowiedzi"]):
                raise ValueError
        except:
            print("Niepoprawna wartość."
                "Wprowadź naturalną liczbę od 1 do {}\n"
                .format(len(dane["odpowiedzi"])))
            return AskModule.zapytaj(dane, flag = False)
            # zaczyna od razu od miejsca gdzie rzucono Error
        
        if choice == dane['poprawna_odp']:
            return 2
        else:
            return -1

    def test(self,questions):
        print('\nKrótkie wprowadzenie:\n1. Wprowadzaj tylko symnbol (A/a/1) '
            'odpowiadający poprawnej odpowiedzi.\n2. Poprawna odpowiedź daje'
            '2 pkt.\n3. Za złą odpowiedź dostajesz -1\nTest zaraz się zacznie.'
            'Powodzenia!')
        time.sleep(1)
        for key, meta in questions.items():
            if key in ("Ilość pytań",):
                continue
            else:
                print("\nPytanie {}:".format(key))
                self.score += self.zapytaj(meta)
        print('\n{:_^80s}\n'.format("KONIEC"))
        print('{} twój wynik: {}'.format(self.name, self.score))
        self.rebegin_prompt(1)
    
    @staticmethod
    def load_question(filename):
        """
        Wczytuje pytania z wybranego pliku JSON 
        """
        qs = None
        with open(filename, "r", encoding='utf8') as read_file:
            qs = json.load(read_file)
        return (qs)

    def play_quiz(self):
        flag = 1
        try:
            for x in range(len(aq.TOPICS_LIST)):
                print("({})-> {}".format(x+1,aq.TOPICS_LIST[x]))
            print("(+)-> Dodać pytanie")
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
            self.test(self.load_question(os.path.join(sys.path[0],
                'Pytania',aq.TOPICS_LIST[choice-1]+'.json')))
        elif flag == -1:
            self.play_quiz() # od nowa jeżeli flaga = True
        elif flag == 0:
            self.rebegin_prompt()

    
    def rebegin_prompt(self, flag = 0):
        print("\nCzy chcesz kontynuować?\nA. Tak\nB. Nie")
        play = input()
        if play.lower() in ['b', 'n','nie']:
            return print('{:~^80s}'.format("ZAPRASZAM PONOWNIE"))
        
        if play.lower() in ['a', 't', 'tak']:
            if flag:
                print("\n\nWybierz dziedzinę pytań:")
            self.play_quiz()
        else:
            print("\nNie rozumiem, chyba literówka.\nNaciśnij T aby zagrać,"
            " czy N aby wyjść.\n")
            self.rebegin_prompt(1)


