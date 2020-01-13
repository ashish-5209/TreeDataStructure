from queue import Queue
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left(root):
    q = Queue()
    q.put(root)

    while q.empty() is False:
        n = q.qsize()
        for i in range(n):
            temp = q.get()
            if i == 0:
                print(temp.data, end=" ")
            if temp.left:
                q.put(temp.left)
            if temp .right:
                q.put(temp.right)

def right(root):
    q = Queue()
    q.put(root)

    while q.empty() is False:
        n = q.qsize()
        for i in range(n):
            temp = q.get()
            if i == n-1:
                print(temp.data, end=" ")
            if temp.left:
                q.put(temp.left)
            if temp .right:
                q.put(temp.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right =Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12)

left(root)
print()
right(root)
