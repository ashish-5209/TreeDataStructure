class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def balanceTree(root):
    if root is None:
        return 0

    lh = balanceTree(root.left)
    if lh == -1:
        return -1
    rh = balanceTree(root.right)
    if rh == -1:
        return -1

    if abs(lh - rh) > 1:
        return -1
    return max(lh, rh) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

if balanceTree(root) >= 0:
    print("Tree if balanced")
else:
    print("Tree is not balanced")
