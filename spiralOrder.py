class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printSpiralLevelOrder(root):
    # Code here

    if (root == None):
        return

    s1 = []
    s2 = []

    s1.append(root)

    while not len(s1) == 0 or not len(s2) == 0:

        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.data, end = " ")

            if (temp.right):
                s2.append(temp.right)
            if (temp.left):
                s2.append(temp.left)

        while (not len(s2) == 0):
            temp = s2[-1]
            s2.pop()
            print(temp.data, end = " ")

            if (temp.left):
                s1.append(temp.left)
            if (temp.right):
                s1.append(temp.right)

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)

printSpiralLevelOrder(root)
