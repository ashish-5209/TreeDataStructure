class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(root, s, lis):
    if root is None:
        return False
    if root.left is None and root.right is None:
        if root.data == s:
            lis.append(root.data)
            return True
        else:
            return False
    if check(root.left, s-root.data, lis):
        lis.append(root.data)
        return True
    if check(root.left, root.data, lis):
        lis.append(root.data)
        return True
    return False

s = 21
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)
lis = []

print(check(root, s, lis))
print(lis)
