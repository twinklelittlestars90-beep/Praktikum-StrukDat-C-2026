class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    #====  Soal 1  ====
    # Menambah node di akhir
    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            return

        # Cari node terakhir
        current = self.head
        while current.next:
            current = current.next

        # Hubungkan node terakhir dengan node baru
        current.next = new_node
        new_node.prev = current
    
    def tampilkan_maju(self):
        # Cari node terakhir
        current = self.head
        print("[Maju]")
        while current:
            print(current.data)
            current = current.next

    #====  Soal 2  ====
    def tampilkan_mundur(self):
        current = self.head

        # Pergi ke node terakhir
        while current and current.next:
            current = current.next
        print("\n[Mundur]")
        # Tampilkan mundur
        while current:
            print(current.data)
            current = current.prev

    def hapus_kendaraan(self, plat):
        current = self.head

        while current:
            if current.data == plat:
                # Jika node pertama
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                  # Menghubungkan node sebelumnya dengan node berikutnya
                    current.prev.next = current.next

                    if current.next:
                      # Menghubungkan node berikutnya dengan node sebelumnya
                        current.next.prev = current.prev
                return

            current = current.next
dll = DoublyLinkedList()
dll.tambah_kendaraan("B 1234 ABC")
dll.tambah_kendaraan("A 1234 ABC")
dll.tambah_kendaraan("C 1234 ABC")
print("[====  Soal 1  ====]")
dll.tampilkan_maju()
dll.tampilkan_mundur()


print("\n\n[====  Soal 2  ====]")
print("Sebelum:")
dll.tampilkan_maju()
dll.hapus_kendaraan("A 1234 ABC")
print("\nSesudah:")
dll.tampilkan_maju()


        