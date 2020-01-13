class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):

    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def diameter(root):

    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    ld = diameter(root.left)
    rd = diameter(root.right)

    return max(lh + rh + 1, max(ld, rd))

def diameter1(root):

    def deepestLength(node, maxD):
        if (node is None):
            return 0, maxD

        leftL, leftMaxD = deepestLength(node.left, maxD)
        rightL, rightMaxD = deepestLength(node.right, maxD)

        length = 1 + (leftL if leftL > rightL else rightL)
        maxDistance = max(leftMaxD, rightMaxD, maxD, 1 + leftL + rightL)
        return length, maxDistance

    _, maxDistance = deepestLength(root, 0)
    return maxDistance

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Diameter of given binary tree is %d" %(diameter(root)))
print("Diameter of given binary tree is %d" %(diameter1(root)))
