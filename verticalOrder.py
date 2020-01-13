import collections
from queue import Queue

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def verticalTravversal(root):
    if root is None:
        return

    q = Queue()
    m = {}
    hd_node = {}

    q.put(root)
    hd_node[root] = 0
    m[0] = [root.data]

    while q.empty() is False:

        temp = q.get()
        if temp.left:
            q.put(temp.left)
            hd_node[temp.left] = hd_node[temp] - 1
            hd = hd_node[temp.left]

            if hd not in m:
                m[hd] = []

            m[hd].append(temp.left.data)

        if temp.right:
            q.put(temp.right)
            hd_node[temp.right] = hd_node[temp] + 1
            hd = hd_node[temp.right]

            if hd not in m:
                m[hd] = []
            m[hd].append(temp.right.data)

    for i in sorted(m):
        print(*m[i], end=' ')
        print()


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

verticalTravversal(root)
