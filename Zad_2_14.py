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
longest = max(list,key=len)
print('Najdłuższy wyraz - "%s"' % longest)
print('Długość najdłuższego wyrazu - %s' % len(longest))