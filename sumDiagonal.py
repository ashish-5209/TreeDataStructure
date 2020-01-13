from collections import defaultdict
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diagonal(root):
    d = defaultdict(lambda:[])
    diagonalUtil(root, 0, d)

    for i in sorted(d):
        print(sum(d[i]), end=" ")
    print()

def diagonalUtil(root, l, d):
    if root:
        d[l].append(root.data)
        diagonalUtil(root.left, l+1, d)
        diagonalUtil(root.right, l, d)

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(9)
    root.left.right = newNode(6)
    root.right.left = newNode(4)
    root.right.right = newNode(5)
    root.right.left.right = newNode(7)
    root.right.left.left = newNode(12)
    root.left.right.left = newNode(11)
    root.left.left.right = newNode(10)

    diagonal(root)
