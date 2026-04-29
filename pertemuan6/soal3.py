class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def tampilkan_antrean(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def sisipkan_vip(head, plat_target, plat_baru):
  if plat_target == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(plat_target - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  plat_baru.next = currentNode.next
  currentNode.next = plat_baru
  return head

node1 = Node('B 2021 ZZZZ')
node2 = Node('D 2035 FFFF')
node3 = Node('BM 1919 SSSS')
node4 = Node('B 30999 TTTT')

node1.next = node2
node2.next = node3
node3.next = node4

newNode = Node('B 5000 DDDD')
node1 = sisipkan_vip(node1, 2, newNode)

print("\nAfter insertion:")
tampilkan_antrean(node1)
