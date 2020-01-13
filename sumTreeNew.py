class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isLeef(root):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    return False

def subTree(root):

    if root is None or isLeef(root):
        return False

    if root.left and root.right:
        if root.left is None:
            ls = 0
        elif isLeef(root.left):
            ls = root.left.data
        else:
            ls = 2*root.left.data

        if root.right is None:
            rs = 0
        elif isLeef(root.right):
            rs = root.right.data
        else:
            rs = 2*root.right.data

        if root.data == rs + ls:
            return True
        else:
            return False
    return False

root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

print(subTree(root))
