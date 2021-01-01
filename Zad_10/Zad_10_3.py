class Stack_uniq:
    """Klasa ma reprezentować stos do przechowywania liczb całkowitych (od 0) bez powtórzeń"""

    def __init__(self, size=20):
        self.items = size * [None]      # utworzenie tablicy
        self.uniq = size*[0]
        self.n = 0                      # liczba elementów na stosie
        self.size = size                

    def is_empty(self):
        return not self.n

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if not isinstance(data, int):
            raise ValueError("Nie poprawna wartość. Liczba niecałkowita")
        if self.uniq[data]:
            #raise ValueError("Ta wartość już jest na stosie")
            #return print("Ta wartość już jest na stosie")
            return None
        self.items[self.n] = data
        self.n += 1
        self.uniq[data] = 1

    def pop(self):
        if self.is_empty():
            return None
        self.n -= 1
        data = self.items[self.n]
        self.uniq[data] = 0
        self.items[self.n] = None    # usuwam referencję
        return data