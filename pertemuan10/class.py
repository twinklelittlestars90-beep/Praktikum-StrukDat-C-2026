class StackList:
  def __init__(self):
    self.stack = []#menggunakan list bawaan Python

  def push(self, url):
    self.stack.append(url)#menggunakan append untuk menambahkan url ke dalam list

  def pop(self):
    if self.isEmpty():#memeriksa apakah list kosong
      return "Riwayat kosong"
    return self.stack.pop()#jika list tidak kosong, url terbaru akan dihapus

  def peek(self):
    if self.isEmpty():#memeriksa apakah list kosong, mengembalikan None jika kosong
      return None
    return self.stack[-1]#mengembalikan url terbaru jika list berisi

  def isEmpty(self):
    return len(self.stack) == 0#memeriksa apakah list kosong

  def size(self):
    return len(self.stack)#mengggunakan len untuk menghitung panjang list

# Create a stack
myStack = StackList()

myStack.push('https://www.google.com')
myStack.push('https://www.google.com')
myStack.push('https://www.google.com')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())
