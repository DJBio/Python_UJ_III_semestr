print('Cześć użytkowniku')

try:
    x = int(input('Proszę o podanie długości prostokąta\n'))
    y = int(input('Proszę o podanie szerokości prostokąta\n'))
    
    unit_1 = '---+'
    unit_2 = '   |'
    
    elem_1 = '+' + unit_1*x + '\n'
    elem_2 = '|' + unit_2*x + '\n'
    rect = '\n' + (elem_1 + elem_2)*y + elem_1

    print(rect)
except ValueError:
    print("Proszę o podanie liczby całkowitej\n")