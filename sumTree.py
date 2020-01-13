class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def s1(root):
    if root is None:
        return 0
    return s1(root.left) + root.data + s1(root.right)

def subTree(root):
    ls = 0
    rs = 0

    if root is None or (root.left is None and root.right is None):
        return True

    ls = s1(root.left)
    rs = s1(root.right)

    if ((root.data == ls+rs) and subTree(root.left) and subTree(root.right)):
        return True

    return False

root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

print(subTree(root))
