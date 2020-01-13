
class Node:

	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key,end=" ")
		inorder(root.right)


def insert( node, key):

	if node is None:
		return Node(key)

	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	return node

def minValueNode( node):
	current = node

	while(current.left is not None):
		current = current.left

	return current

def deleteNode(root, key):
	if root is None:
		return None
	if root.key > key:
		root.left = deleteNode(root.left, key)
	elif root.key < key:
		root.right = deleteNode(root.right, key)
	else:
		if root.left is None:
			return root.right
		elif root.right is None:
			return root.left
		else:
			temp = minValueNode(root.right)
			root.key = temp.key
			root.right = deleteNode(root.right, temp.key)
	return root

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

inorder(root)
print()
root = deleteNode(root, 20)
inorder(root)
print()
root = deleteNode(root, 30)
inorder(root)
print()
root = deleteNode(root, 50)
inorder(root)
