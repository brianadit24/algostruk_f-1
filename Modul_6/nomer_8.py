class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambahkan(self, data_baru):
        new_node = Node(data_baru)

        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def pengurut(self, awal, akhir):
        hasil = None

        if awal == None:
            return akhir
        if akhir == None:
            return awal

        if awal.data <= akhir.data:
            hasil = awal
            hasil.next = self.pengurut(awal.next, akhir)
        else:
            hasil = akhir
            hasil.next = self.pengurut(awal, akhir.next)
        return hasil

    def cariMid(self, head):
        if (head == None):
            return head
        
        a = head
        b = head

        while b.next is not None and b.next.next is not None:
            a = a.next
            b = b.next.next

        return a

    def mergeSort(self, a):
        if a == None or a.next == None:
            return a

        mid = self.cariMid(a)
        separuhKanan = mid.next

        mid.next = None

        awal = self.mergeSort(a)

        akhir = self.mergeSort(separuhKanan)

        hasil = self.pengurut(awal, akhir)
        return hasil

    def kunjungi(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

        
ll = LinkedList()
ll.tambahkan(34)
ll.tambahkan(23)
ll.tambahkan(12)
ll.tambahkan(1)
ll.tambahkan(86)

ll.head = ll.mergeSort(ll.head)
ll.kunjungi()
