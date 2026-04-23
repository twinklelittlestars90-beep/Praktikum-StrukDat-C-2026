class Node:
  def __init__(self, url):
    self.url = url
    self.next = None

class StackLinkedList:
  def __init__(self):
    self.top = None
    self.count = 0 #untuk menghitung jumlah riwayat

  def push(self, value):
    new_node = Node(value)#membuat node baru
    if self.top:
      new_node.next = self.top
    self.top = new_node
    self.count += 1

  def pop(self):
    if self.isEmpty():
      return "Riwayat kosong"
    popped_node = self.top
    self.top = self.top.next
    self.count -= 1
    return popped_node.url

  def peek(self):
    if self.isEmpty():
      return "Riwayat kosong"
    return self.top.url

  def isEmpty(self):
    return self.count == 0

  def stackSize(self):
    return self.count

  def traverseAndPrint(self):
    currentNode = self.top
    while currentNode:
      print(currentNode.url, end=" -> ")
      currentNode = currentNode.next
    print()

myStack = StackLinkedList()
myStack.push('https://www.google.com')
myStack.push('https://www.google.com')
myStack.push('https://www.google.com')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
