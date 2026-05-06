class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        print(f"[INSERT] Berhasil memasukkan: ID {data[0]} - {data[1]}")

    def insert(self, node, data):
        if data[0] < node.data[0]:
            if node.left is None:
                node.left = TreeNode(data)
                print(f"[INSERT] Berhasil memasukkan: ID {data[0]} - {data[1]}")
            else:
                self.insert(node.left, data)  
        elif data[0] > node.data[0]:
            if node.right is None:
                node.right = TreeNode(data)
                print(f"[INSERT] Berhasil memasukkan: ID {data[0]} - {data[1]}")
            else:
                self.insert(node.right, data)  
        
    def traversal_inorder(self, node, i=[1]):
        if node is not None:
            self.traversal_inorder(node.left,i)  
            print(f"{i}. {node.data[0]} - {node.data[1]}")
            i[0]+=1
            self.traversal_inorder(node.right,i)
            
    def search(self, node, target):
        if node is None:
           return None
        elif node.data[0] == target:
           print(f"[SEARCH] Mencari ID {target}... Ditemukan! Judul: {node.data[1]}")
        elif target < node.data[0]:
           return self.search(node.left, target)
        else:
           return self.search(node.right, target)
        
    def get_min(self, node):
        if node is None:
            print("[STATISTIK] Tree kosong")
            return None
        current = node
        while current.left is not None:
            current = current.left
        print(f"[STATISTIK] ID Terkecil: {current.data[0]}")
        return current

    def get_max(self, node):
        if node is None:
            print("[STATISTIK] Tree kosong")
            return None
        current = node
        while current.right is not None:
            current = current.right
        print(f"[STATISTIK] ID Terbesar: {current.data[0]}")
        return current
    
    def height(self, node):
        if node is None:
            return -1 
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

tree = BinaryTree()
print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG" \n========================================= ')
tree.insert_root([50, "Dasar Pemrograman"])
tree.insert(tree.root,[30, "Struktur Data"])
tree.insert(tree.root,[70, "Kecerdasan Buatan"])
tree.insert(tree.root,[20, "Matematika Diskrit"])
tree.insert(tree.root,[40, "Basis Data"])
tree.insert(tree.root,[60, "Jaringan Komputer"])
tree.insert(tree.root,[80, "Sistem Operasi"])

print("\n[INFO] Koleksi Buku (In-Order Traversal): ")
tree.traversal_inorder(tree.root)
print('\n')

tree.search(tree.root, 10)

tree.get_min(tree.root).data
tree.get_max(tree.root).data

height = tree.height(tree.root)
print(f"[INFO] Tinggi (Height) Tree: {height}")
print("========================================= \nSimulasi Selesai! ")
