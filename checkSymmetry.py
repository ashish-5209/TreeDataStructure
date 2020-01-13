class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 and root2:
        return (root1.data == root2.data) and check(root1.left, root2.left) and check(root1.right, root2.right)
    return False

root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print(check(root1, root2))
