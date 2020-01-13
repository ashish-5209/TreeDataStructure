class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

flag = [0]
def nthPostOrder(root, n):
    if root is None:
        return
    if flag[0] <= n:
        nthPostOrder(root.left, n)
        nthPostOrder(root.right, n)
        flag[0] += 1
        if flag[0] == n:
            print(root.data)
            return

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

nthPostOrder(root, 5)
