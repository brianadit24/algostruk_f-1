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

a = Node(11)
b = Node(12)
c = Node(13)
d = Node(15)
e = Node(16)

a.next = b
b.next = c
c.next = d
d.next = e

llist = LinkedList(a)

print(llist.cari(a,13))