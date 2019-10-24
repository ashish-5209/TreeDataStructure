from queue import Queue
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def twoLevelTraversal(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data)
        return
    q = Queue()
    lis = []
    temp = None
    sz = 0
    ct = 0
    rightToLeft = False
    q.put(root)

    while q.empty() == False:

        ct += 1
        sz = q.qsize()

        for i in range(sz):
            temp = q.get()
            if rightToLeft == False:
                print(temp.data, end=" ")
            else:
                lis.append(temp)
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
        if rightToLeft == True:
            while len(lis) != 0:
                temp = lis[-1]
                lis.pop()
                print(temp.data, end=" ")

        if ct == 2:
            rightToLeft = not rightToLeft
            ct = 0
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(3)
root.left.right.right = Node(1)
root.right.left.left = Node(4)
root.right.left.right = Node(2)
root.right.right.left = Node(7)
root.right.right.right = Node(2)
root.left.right.left.left = Node(16)
root.left.right.left.right = Node(17)
root.right.left.right.left = Node(18)
root.right.right.left.right = Node(19)

twoLevelTraversal(root)
