from random import randrange
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class RandomQueue_2:
    '''Kolejka losowa oparta na liście jednokierunkowej'''
    def __init__(self):
        self.head = None
        self.n = 0 #liczba elementów w kolejce
        
    def insert(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.n +=1
            return None #"Pierwszy element"
        gdzie = randrange(self.n+1)
        #print ("Gdzie: ", gdzie)
        if gdzie == 0:
            self.head = Node(item, self.head)
            self.n +=1
            return None

        tu_2 = self.head
        tu_1 = None
        while gdzie:
            gdzie -= 1
            tu_1 = tu_2
            tu_2 = tu_2.next
        tu_1.next = Node(item, tu_2)
        self.n +=1

    def is_empty(self):
        return not self.head

    def remove(self):   # zwraca losowy element
        if self.is_empty():
            raise Exception("Kolejka jest pusta")
        data = self.head.data
        self.head = self.head.next
        self.n -= 1
        return data


    def is_full(self):
        return False          # W tej implementacji to nie jest możliwe

    def clear(self):     # czyszczenie listy
        self.n = 0
        while self.head:
            next = self.head.next
            del self.head.next
            self.head = next

if __name__ == "__main__":
    pq_2 = RandomQueue_2()
    for item in [1,2,3,4,5]:
        pq_2.insert(item) 
    while not pq_2.is_empty():
        print(pq_2.remove())