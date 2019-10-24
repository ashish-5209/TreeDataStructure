class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def spiarlTraversal(root):

    if root is None:
        return

    s1 = []
    s2 = []

    s1.append(root)

    while not len(s1) == 0 or not len(s2) == 0:

        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.data, end=" ")

            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while not len(s2) == 0:
            temp = s2[-1]
            s2.pop()
            print(temp.data, end=" ")

            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

spiarlTraversal(root)
