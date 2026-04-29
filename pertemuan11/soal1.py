class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.count = 0

  def enqueue(self, data):
    new_node = Node(data)
    if self.rear is None:
      self.front = self.rear = new_node
      self.count += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.count += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.count -= 1
    if self.front is None:
      self.rear = None
    print (f'Dokter memanggil:{temp.data[0]}--{temp.data[1]}')
    return temp.data

  def peek(self):
    if self.isEmpty():
      return "Antrian masih kosong"
    print(f'Pasien berikutnya: {self.front.data[0]}--{self.front.data[1]}')

  def isEmpty(self):
    return self.count == 0

  def size(self):
    print(f'Jumlah pasien menunggu: {self.count} orang')

  def printQueue(self):
    temp = self.front
    i=1
    while temp:
      print(f"{temp.data[0]} terdaftar dengan keluhan: {temp.data[1]} (No. Antrian: {i})")
      temp = temp.next
      i+=1
  def clear(self):
    temp = self.front
    i=1
    while temp:
      Queue.dequeue(self)
      temp = temp.next
    return 'sesi klinik selesai, antrian dikosongkan'
    

# Create a queue
myQueue = Queue()

print("====================================\nSISTEM ANTRIAN POLI UMUM  \nRS Sehat Bersama  \n====================================")

print("Apakah antrian kosong?")

if myQueue.isEmpty():
  print("YA, antrian masih kosong.")
myQueue.enqueue(['Budi','Demam Tinggi'])
myQueue.enqueue(['Ani','Batuk pilek'])
myQueue.enqueue(['Citra','Sakit kepala'])
myQueue.size()
myQueue.peek()
myQueue.dequeue()
myQueue.enqueue(["Dodi", "nyeri perut"])
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()
print(myQueue.clear())
print("Apakah antrian kosong?")
if myQueue.isEmpty():
  print("YA, antrian masih kosong.")
else:
  print('YA, antrian sudah kosong.')
print('====================================  \nSimulasi Selesai!\n====================================')