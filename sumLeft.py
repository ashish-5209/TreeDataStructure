class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isLeft(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

def leftSum(root):
    res = 0

    if root:
        if isLeft(root.left):
            res += root.left.data
        else:
            res += leftSum(root.left)
        res += leftSum(root.right)
    return res

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)

print(leftSum(root))
