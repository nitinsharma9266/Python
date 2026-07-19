
        
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root is None

    def insertdata(self, root, value):
        if root is None:
            return Node(value)

        if value == root.item:
            print("Duplicate value is not allowed")
        elif value < root.item:
            root.left = self.insertdata(root.left, value)
        else:
            root.right = self.insertdata(root.right, value)

        return root

    def insert(self, value):
        self.root = self.insertdata(self.root, value)

    def traverse(self, root):
        if root is None:
            
            return
        self.traverse(root.left)
        print(root.item, end=" ")
        self.traverse(root.right)

    def search(self, root, value):
        if root is None:
            print(f"{value} Not found")
            return
        if root.item == value:
            print(f"{value} is found")
        elif value < root.item:
            self.search(root.left, value)
        else:
            self.search(root.right, value)
    def size(self,root):
        if root is None:
            return 0
        
        return 1+self.size(root.left)+self.size(root.right)
            
bst=BST()
# ---- Testing ----
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

bst.traverse(bst.root)
print()
bst.search(bst.root,80)
print()
print(bst.size(bst.root))


