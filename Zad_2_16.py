line = '''
    Napisy są z reguły jednowierszowe.
Jeśli jednak masz taką potrzebę,
to możesz tworzyć napisy wielowierszowe.
Tworzysz je dodając na początku i 
końcu ciągu znaków potrójne apostrofy
                        - GvR
'''
print(line)
line_full = line.replace('GvR',"Guido van Rossum")
print(line_full)