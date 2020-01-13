class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
inorder(root)
print()
mirror(root)
inorder(root)
