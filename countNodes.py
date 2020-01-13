class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodes(root):

    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
print(countNodes(root))
