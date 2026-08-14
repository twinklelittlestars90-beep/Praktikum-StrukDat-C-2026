class HashTable:
    def __init__(self):
        self.my_list = [None] * 10

    def hash_function(self, value):
        total = 0
        for char in value:
            total += ord(char)
        return total % 10
    
    def insert(self, kode, name):
        index = self.hash_function(kode)
        self.my_list[index] = [kode, name]

    def search(self, kode):
        index = self.hash_function(kode)
        if self.my_list[index] is None:
            return False
        return self.my_list[index][0] == kode

    def delete(self, kode):
        index = self.hash_function(kode)

        if self.my_list[index] is None:
            return False

        if self.my_list[index][0] == kode:
            self.my_list[index] = None
            return True

        return False

    def display(self):
        for i in range(len(self.my_list)):
            print(f"{i+1}. {self.my_list[i]}")

ht= HashTable()
ht.insert("BK111", "Mahir C Dalam Satu Jam")
ht.insert("BK222", "Python Dasar")
ht.insert("BK33", "Matematika Diskrit")
ht.insert("BK444", "Atomic Habit")
ht.display()
ht.insert("BK045", "Mein Kamp")
ht.insert("BK111", "Bumi Manusia")
ht.display()
print(ht.search("BK111"))
print(ht.search("ABCD"))
ht.delete("BK222")
ht.display()