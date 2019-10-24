from queue import Queue
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def inorderIterative(root):
    if root is None:
        return

    current = root
    s = []

    while True:
        if current is not None:
            s.append(current)
            current = current.left

        elif(s):
            current = s.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break

def preOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def preOrderIterative(root):
    if root is None:
        return
    lis = []
    lis.append(root)
    while len(lis) != 0:
        temp = lis.pop()
        print(temp.data, end=" ")
        if temp.right:
            lis.append(temp.right)
        if temp.left:
            lis.append(temp.left)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")

def postOrderIterative(root):
    if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)

    while s1:
        temp = s1.pop()
        s2.append(temp)
        if temp.left:
            s1.append(temp.left)
        if temp.right:
            s1.append(temp.right)
    while s2:
        temp = s2.pop()
        print(temp.data, end=" ")

def postOrderIterativeOneStack(root):
    if root is None:
        return
    lis = []
    curr = root
    while curr is not None or len(lis) != 0:
        if curr != None:
            lis.append(curr)
            curr = curr.left
        else:
            temp = lis[-1].right
            if temp is None:
                temp = lis.pop()
                print(temp.data, end=" ")

                while len(lis) != 0 and temp == lis[-1].right:
                    temp = lis.pop()
                    print(temp.data, end=" ")
            else:
                curr = temp

def levelOrder(root):
    if root is None:
        return
    q = Queue()
    q.put(root)
    while q.empty() is False:
        temp = q.get()
        print(temp.data, end=" ")

        if temp.left:
            q.put(temp.left)
        if temp.right:
            q.put(temp.right)

def levelOrderLine(root):
    if root is None:
        return
    q = Queue()
    q.put(root)
    q.put("@")
    while q.empty() is False:
        temp = q.get()
        if temp is "@":
            if q.empty() is False:
                q.put("@")
                print()
        else:
            if temp != "@" and temp.left:
                q.put(temp.left)
            if temp != "@" and temp.right:
                q.put(temp.right)

            print(temp.data, end=" ")

def levelOrderLineNew(root):
    if root is None:
        return
    q = Queue()
    q.put(root)

    while q.empty() == False:

        n = q.qsize()
        while n > 0:
            temp = q.get()
            print(temp.data, end= " ")
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)

            n -= 1
        print(' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

inorder(root)
print()
inorderIterative(root)
print()
preOrder(root)
print()
preOrderIterative(root)
print()
postOrder(root)
print()
postOrderIterative(root)
print()
postOrderIterativeOneStack(root)
print()
levelOrder(root)
print()
levelOrderLine(root)
print()
levelOrderLineNew(root)
