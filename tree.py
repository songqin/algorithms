class TreeNode:
	def __init__(self, v):
		self.value=v
		self.left, self.right=None, None

class Traversal(object):
	def __init__(self):
		self.traverse_path=list()
	def preorder(self, root):
		if root:
			
