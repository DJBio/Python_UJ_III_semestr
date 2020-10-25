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
print('Ilość słow w napisie - %s' % len(list))