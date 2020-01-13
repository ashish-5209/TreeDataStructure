
class addNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def rightLeafSum(root, Sum):
	if(not root):
		return

	if(root.right):
		if(not root.right.left and
		not root.right.right):
			Sum[0] += root.right.data

	rightLeafSum(root.left, Sum)
	rightLeafSum(root.right, Sum)

if __name__ == '__main__':

	root = addNode(1)
	root.left = addNode(2)
	root.left.left = addNode(4)
	root.left.right = addNode(5)
	root.left.left.right = addNode(2)
	root.right = addNode(3)
	root.right.right = addNode(8)
	root.right.right.left = addNode(6)
	root.right.right.right = addNode(7)

	Sum = [0]
	rightLeafSum(root, Sum)
	print(Sum[0])
