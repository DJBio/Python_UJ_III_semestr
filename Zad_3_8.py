A = set('Definicja funkcji tworzy obiekt funkcji.')
B = set('W Pythonie nie ma deklaracji typu argumentów.')
uniq = list(A.intersection(B))
uniq.sort()
print ('Jednocześnie występujące znaki: ',uniq)
all = list(A.union(B))
all.sort(key=str.lower)
print ('Wspólna lista zanków', all)