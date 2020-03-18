class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def cari(self, head, yang_dicari):
        while head is not None:
            if head.data == yang_dicari:
                return True
            head = head.next
        return False

    def tambahDepan(self, head):
        head.next = self.head
        self.head = head

    def tambahAkhir(self, head):
        node = self.head
        while node.next != None:
            node = node.next
        node.next = head

    def tambah(self, head, posisi):
        head.next = posisi.next
        posisi.next = head

    def hapus(self, posisi):
        node = self.head
        while node is not None:
            if node.next == posisi:
                node.next = posisi.next
            node = node.next

    def kunjungi(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        print()

z = Node('Abdul Crimping')
a = Node('Rahmat')
b = Node('Herman')
c = Node('Maul')
d = Node('Bambang')
e = Node('Agus')
f = Node('Budi')
x = Node('Ahmad al Python')
y = Node('Agus Bootloop')

a.next = b
b.next = c
c.next = d
d.next = e

linked = LinkedList()
linked.head = a

linked.tambahDepan(y)
linked.kunjungi()
linked.tambahAkhir(x)
linked.kunjungi()
linked.tambah(z, b)
linked.kunjungi()
linked.hapus(c)
linked.kunjungi()
print(linked.cari(b, 'Agus'))
print(linked.cari(b, 'Maul'))