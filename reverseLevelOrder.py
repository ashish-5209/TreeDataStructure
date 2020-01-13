from queue import Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reverseOrder(root):
    if root is None:
        return
    q = Queue()
    lis = []

    q.put(root)
    while q.empty() == False:
        temp = q.get()
        lis.append(temp)
        if temp.right:
            q.put(temp.right)
        if temp.left:
            q.put(temp.left)

    while len(lis) != 0:
        temp = lis.pop()
        print(temp.data, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
reverseOrder(root)
