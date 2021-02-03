from ask_module import AskModule

def begin_prompt(flag = 1):
    if flag:
        print("Witam użytkowniku!")
    user = input("Wpisz swoje imię czy nick:\n")
    if len(user) >= 2 :
        AskModule(user)
        #am.play_quiz()
    else:
        print('Zbyt krótkie imię, wprowadź powyżej 2 znaków')
        begin_prompt(0)
        

if __name__ == '__main__':

    begin_prompt()