class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth(node):
    d = 0
    while node != None:
        d += 1
        node = node.left

    return d
def check(root, d, level):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return (d == level+1)

    if root.left is None or root.right is None:
        return False
    return check(root.left, d, level+1) and check(root.right, d, level+1)

if __name__ == '__main__':
    root = None
    root = newNode(10)
    root.left = newNode(20)
    root.right = newNode(30)

    root.left.left = newNode(40)
    root.left.right = newNode(50)
    root.right.left = newNode(60)
    root.right.right = newNode(70)
    d = depth(root)
    print(check(root, d, 0))
