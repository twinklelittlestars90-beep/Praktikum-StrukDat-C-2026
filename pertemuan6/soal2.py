class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def hapusKendaraan(head, plat):
  if head == plat:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != plat:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next
  return head

def tambahKendaraan(head, plat):
  currentNode=head
  while currentNode.next!=None:
     currentNode=currentNode.next
  currentNode.next=plat
  return head
node1 = Node('B 2021 ZZZZ')
node2 = Node('D 2035 FFFF')
node3 = Node('BM 1919 SSSS')
node4 = Node('B 30999 TTTT')

node1.next = node2
node2.next = node3
node3.next = node4

node1=hapusKendaraan(node1, node2)
print("\nAfter delete:")
traverseAndPrint(node1)

newNode = Node('B 5000 DDDD')
node1 = tambahKendaraan(node1, newNode)

print("\nAfter insertion:")
traverseAndPrint(node1)
