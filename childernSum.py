class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def children(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    s = 0
    if root.left:
        s += root.left.data
    if root.right:
        s += root.right.data

    if (root.data == s) and children(root.left) and children(root.right):
        return True
    else:
        return False

if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(8)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode(2)

    print(children(root))
