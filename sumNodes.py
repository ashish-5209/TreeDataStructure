class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumTree(root):
    if root is None:
        return 0
    return root.data + sumTree(root.left) + sumTree(root.right)

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

print(sumTree(root))
