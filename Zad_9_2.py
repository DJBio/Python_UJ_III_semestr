class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "Węzeł o kluczu: {}".format(self.data)
        
class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.is_empty():
            return None
        node = self.head
        D = ""
        while node:
            D += "Węzeł o kluczu: {}".format(node.data) + '\n'
            node = node.next
        return D

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(n)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
    
# Nowe metody 
    
    def search(self, data):
        if self.is_empty():
            return None
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None
        
    def find_min(self):
        """Zwraca pierwszy najmniejszy element zaczynając od głowy listy"""
        if self.is_empty():
            return None
        
        min = node = self.head
        while node:
            if node.data < min.data:
                min = node
            node = node.next
        return min
        
    def find_max(self):
        """Zwraca pierwszy największy element zaczynając od głowy listy"""
        if self.is_empty():
            return None
        
        max = node = self.head
        while node:
            if node.data > max.data:
                max = node
            node = node.next
        return max
    
    def reverse(self):
        """Odwrócenie kolejności elementów na liście"""
        ostatni = None
        self.tail = ten = self.head
        while ten:
            next = ten.next
            ten.next = ostatni
            ostatni = ten
            ten = next
        self.head = ostatni
        return self
    
    
pusta_lista = SingleList()

Lista = SingleList()
for x in range(11):
    Lista.insert_head(Node(x))      
Lista.insert_head(Node(-3))
for x in range(3,18,2):
    Lista.insert_head(Node(x))

print(pusta_lista.search(1))
print(pusta_lista.find_min())
print(Lista.search(1))
print(Lista.search(100))
print(Lista.find_min())
print(Lista.find_max())   
