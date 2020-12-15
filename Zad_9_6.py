class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "Węzeł o kluczu: {}".format(self.data)

def tp(top, level=0):
    if top is None:
        return None
    tp(top.right, level+1)
    print ( "{}* {}".format('   '*level, top) )
    tp(top.left, level+1)

def count_leafs(top):
    if top is None: 
        return 0 
    if top.left is None and top.right is None: 
        return 1 
    else: 
        return count_leafs(top.left) + count_leafs(top.right)
        
def count_total(top):
    if top is None: 
        return 0 
    if top.left is None and top.right is None: 
        return top.data
    else: 
        return top.data + count_total(top.left) + count_total(top.right)    

def display_aux(top): #f-ja ta jest oparta na kodzie z forum stackoverflow.com, trochę zmieniono kod pod nasze zmienne oraz brak klasy; dodano gdyż chciałem zwizualizować dane
        """Returns list of strings, width, height, and horizontal coordinate of the root.""" 
        # No child.
        if top.right is None and top.left is None:
            line = '%s' % top.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if top.right is None:
            lines, n, p, x = display_aux(top.left)
            s = '%s' % top.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if top.left is None:
            lines, n, p, x = display_aux(top.right)
            s = '%s' % top.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display_aux(top.left)
        right, m, q, y = display_aux(top.right)
        s = '%s' % top.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        
def display(top): #f-ja ta jest oparta na kodzie z forum stackoverflow.com, trochę zmieniono kod pod nasze zmienne oraz brak klasy; dodano gdyż chciałem zwizualizować dane
    lines, *_ = display_aux(top)
    for line in lines:
        print(line)

root = Node(5)

root.left = Node(10)
root.left.left = Node(-5)
root.left.right = Node(8)
root.left.right.left = Node(7)

root.right = Node(20)
root.right.right = Node(13) 
root.right.right.left = Node(18) 
root.right.right.right = Node(14)
root.right.right.right.right  = Node(10)
root.right.right.right.left  = Node(0)

display(root) 
print('Ilość węzłów: ',count_leafs(root))
print('Suma kluczy: ',count_total(root))