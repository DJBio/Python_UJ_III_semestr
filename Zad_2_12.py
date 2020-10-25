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
list_first=[]
list_last=[]
for x in list:
    list_first.append(x[0])
    list_last.append(x[len(x)-1])
#print(list_first)
#print(list_last)
Str_first = ''.join(str(x) for x in list_first)
Str_last = ''.join(str(x) for x in list_last)
print('Napis z pierwszych znaków: %s' % Str_first)
print('Napis z ostatnich znaków: %s' %Str_last)