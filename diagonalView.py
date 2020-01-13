class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diagonal(root):
    d = dict()
    diagonalUtil(root, 0, d)

    for i in sorted(d):
        print(*d[i], end=' ')
        print()

def diagonalUtil(root, l, d):
    if root is None:
        return

    if l in d:
        d[l].append(root.data)
    else:
        d[l] = [root.data]

    diagonalUtil(root.left, l+1, d)
    diagonalUtil(root.right, l, d)


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonal(root)
