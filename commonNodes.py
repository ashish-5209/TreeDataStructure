class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root, s):
    if root is None:
        return
    inorder(root.left, s)
    if root.data in s:
        print(root.data, end=" ")
    inorder(root.right, s)

def setElements(s, root):
    if root is not None:
        setElements(s, root.left)
        s.add(root.data)
        setElements(s, root.right)


r = Node(5)
insert(r,Node(1))
insert(r,Node(10))
insert(r,Node(0))
insert(r,Node(4))
insert(r,Node(7))
insert(r,Node(9))
r1 = Node(5)
insert(r1,Node(10))
insert(r1,Node(7))
insert(r1,Node(20))
insert(r1,Node(4))
insert(r1,Node(9))
s = set()
setElements(s, r1)
print(s)
inorder(r, s)
print()
