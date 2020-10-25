line = '''
    Napisy są z reguły jednowierszowe.
Jeśli jednak masz taką potrzebę,
to możesz tworzyć napisy wielowierszowe.
Tworzysz je dodając na początku i 
końcu ciągu znaków potrójne apostrofy
'''
sort_alf = sorted(line.split(),key=str.lower)
sort_long = sort_alf[:]
sort_long.sort(key=len,reverse=True)
print('Posortowane wyrazy alfabetycznie: \n%s\n' %sort_alf)
print('Posortowane wyrazy wg długości: \n%s\n' %sort_long)
