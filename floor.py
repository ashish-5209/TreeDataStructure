class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    if root.data > key:
        root.left = insert(root.left, key)
    elif root.data < key:
        root.right = insert(root.right, key)
    return root

def floorBST(node, key):
    temp = None
    while node:
        if node.data == key:
            return node.data
        if node.data > key:
            node = node.left
        else:
            temp = node
            node = node.right
    return temp.data if temp else None

def ceil(node, key):
    temp = None
    while node:
        if node.data == key:
            return node.data
        if node.data < key:
            node = node.right
        else:
            temp = node
            node = node.left
    return temp.data if temp else None

root = Node(50)
insert(root,30)
insert(root,20)
insert(root,40)
insert(root,70)
insert(root,60)
insert(root,80)
print(floorBST(root, 25))
print(ceil(root, 45))
