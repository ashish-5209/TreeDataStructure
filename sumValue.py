class getNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(root, s, x):
    if root is None:
        return
    if (root.left and root.left.data == s) or (root.right and root.right.data == s):
        x[0] += root.data
    check(root.left, s, x)
    check(root.right, s, x)

if __name__ == '__main__':

    # binary tree formation
    root = getNode(4)         #     4
    root.left = getNode(2)         #     / \
    root.right = getNode(5)         #     2 5
    root.left.left = getNode(7)     #     / \ / \
    root.left.right = getNode(2) # 7 2 2 3
    root.right.left = getNode(2)
    root.right.right = getNode(3)

    x = [0]
    check(root, 2, x)
    print(x)
