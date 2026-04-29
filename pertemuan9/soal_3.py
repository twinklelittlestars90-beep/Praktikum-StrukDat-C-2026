class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def tambah_petugas(self, data):
        new_node = Node(data)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Sambungkan node terakhir ke node baru
        current.next = new_node
        new_node.next = self.head

    def giliran_berikutnya(self, giliran):
            if self.head is None:
               print("Linked list kosong")
               return

            current = self.head
            i=0
            while i<giliran:
               print(f"Giliran {i+1}:{current.data}")
               current = current.next
               i+=1

cll=CircularLinkedList()
cll.tambah_petugas("Andi")
cll.tambah_petugas("Budi")
cll.tambah_petugas("Siti")
cll.giliran_berikutnya(7)


            