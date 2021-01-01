class PriorityQueue:
    def cmp (a, b):
        return (a > b) - (a < b)

    def __init__(self, cmpfunc = cmp):
        self.items = []
        self.cmpfunc = cmpfunc
    
    def __str__(self):   # podglądamy kolejkę
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.cmpfunc(self.items[i], self.items[maxi]) == 1:
                maxi = i
        return self.items.pop(maxi)   # mało wydajne
        
pq = PriorityQueue()
for item in [5, 3, 8, 10,7]:
    pq.insert(item)
# Usuwanie elmentów z kolejki w kolejności: 8, 5, 3.
while not pq.is_empty():
    print ( pq.remove() )
    
def wazniejsze(a,b):
    return (a[1] > b[1]) - (a[1] < b[1])
plany = PriorityQueue(wazniejsze)
for item in [("Przygotować pyszne śniadanie",10),("Kupić sobie kolejny prezent:)",5),("Umyć psa",8),("Napisać plan powtórzeń materiału do sesji",7),("Obejrzeć dowolny film A.Hitchcock'a",3)]:
    plany.insert(item)
print("\nPlany na 2 stycznia:")
while not plany.is_empty():
    print ( plany.remove()[0] )





