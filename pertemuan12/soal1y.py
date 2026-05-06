class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
       self.root=None
  def insert_manual(self):
    self.root = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    self.root.left = nodeB
    self.root.right = nodeC

    self.root.left.left = nodeD
    self.root.left.right = nodeE

    self.root.right.right = nodeF
    
  def get_leaf(self,node, leaflist):
    if node:
      if node.left is None and node.right is None:
        leaflist.append(node.data)
      self.get_leaf(node.left, leaflist)
      self.get_leaf(node.right, leaflist)
    return leaflist

def preOrderTraversal(node):
    if node is None:
      return
    print(node.data, end="-")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end="-")
  inOrderTraversal(node.right)

def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end="-")


tree = BinaryTree()
tree.insert_manual()

print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'\n")
print("======================================\n")
print("[INFO] Membangun Struktur Gudang...\n")
print("[INFO] Struktur berhasil dibuat. HASIL AUDIT: ")
print("HASIL AUDIT: ")
print("1. pre_order:")
preOrderTraversal(tree.root)
print("\n")
print("2. in_order:")
inOrderTraversal(tree.root)
print("\n")
print("3. post_order:")
postOrderTraversal(tree.root)
leaves=[]
tree.get_leaf(tree.root, leaves)
print("\n gudang ujung:")
print(leaves)

