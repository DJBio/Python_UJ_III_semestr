line = '''
    Napisy są z reguły jednowierszowe.
Jeśli jednak masz taką potrzebę,
to możesz tworzyć napisy wielowierszowe.
Tworzysz je dodając na początku i 
końcu ciągu znaków potrójne apostrofy
'''
print(line)
line_count=line.strip()
list = line_count.split()
Znaki_cz = sum(len(x) for x in list)
print('Łączna długośc wyrazów - %s' % Znaki_cz)