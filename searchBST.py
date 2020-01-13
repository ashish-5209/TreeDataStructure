class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def searchRecursive(node, data):
    if node is None:
        return False
    if node.data == data:
        return True
    if node.data > data:
        return searchRecursive(node.left, data)
    return searchRecursive(node.right, data)

def searchIterative(node, data):

    while node:
        if node.data == data:
            return True
        if node.data > data:
            node = node.left
        else:
            node = node.right
    return False

def insertRecursive(r1, data):
    if r1 is None:
        return Node(data)
    if r1.data > data:
        r1.left = insertRecursive(r1.left, data)
    if r1.data < data:
        r1.right = insertRecursive(r1.right, data)
    return r1
def insertIterative(root, data):
    temp = Node(data)
    parent = Node
    curr = root
    while curr:
        parent = curr
        if curr.data > data:
            curr = curr.left
        elif curr.data < data:
            curr = curr.right
        else:
            return root
    if parent is Node:
        return temp
    if parent.data > data:
        parent.left = temp
    else:
        parent.right = temp
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

r1 = Node(50)
insertRecursive(r1,30)
insertRecursive(r1,20)
insertRecursive(r1,40)
insertRecursive(r1,70)
insertRecursive(r1,60)
insertRecursive(r1,80)

inorder(r1)
print()
print(searchRecursive(r1, 70))

r2 = Node(50)
insertIterative(r2,30)
insertIterative(r2,20)
insertIterative(r2,40)
insertIterative(r2,70)
insertIterative(r2,60)
insertIterative(r2,80)
inorder(r2)
print()
print(searchIterative(r2, 180))
