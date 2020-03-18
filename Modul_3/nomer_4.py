class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def kunjungi(self):
        node = self.head
        while node is not None:
            print(node.data)
            reverse = node
            node = node.next
        print()
        while reverse is not None:
            print(reverse.data)
            reverse = reverse.prev
        print()
    
    def tambahAwal(self, head):
        head.next = self.head
        self.head = head
        head.next.prev = head
        
z = DNode('Abdul Crimping')
a = DNode('Rahmat')
b = DNode('Herman')
c = DNode('Maul')
d = DNode('Bambang')
e = DNode('Agus')
f = DNode('Budi')
x = DNode('Ahmad al Python')
y = DNode('Agus Bootloop')

a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
d.next = e
e.prev = d
e.next = f
f.prev = e

doubly = DoublyLinkedList()
doubly.head = a

doubly.kunjungi()
doubly.tambahAwal(z)
doubly.kunjungi()