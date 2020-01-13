import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def BSTutil(root, s, m):
    if root is None:
        return True
    if root.data < s or root.data > m:
        return False
    return BSTutil(root.left, s, root.data-1) and BSTutil(root.right, root.data+1, m)
def BST(root):
    return BSTutil(root, -sys.maxsize-1, sys.maxsize)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(BST(root))
