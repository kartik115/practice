import sys


class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


class BinarySearchTree:
	def __init__(self):
		self.root = None

	
	def insert(self, data):
		self.root = self.insertNode(self.root, data)


	def insertNode(self, node, data):
		if node is None:
			return Node(data)

		if node.data > data:
			node.left = self.insertNode(node.left, data)
		elif node.data < data:
			node.right = self.insertNode(node.right, data)

		return node

	
	def findDeadEnd(self, node, minimum, maximum):
		if node is None:
			return False

		if minimum == maximum:
			return True

		return self.findDeadEnd(node.left, minimum, node.data-1) or self.findDeadEnd(node.right, node.data+1, maximum) 

	
	def maxPathSumUtil(self, root, res):   
	    # Base Case 
	    if root is None: 
	        return 0
	      
	    if root.left is None and root.right is None: 
	        return root.data
	      
	    # Find maximumsum in left and righ subtree. Also 
	    # find maximum root to leaf sums in left and righ  
	    # subtrees ans store them in ls and rs 
	    ls = self.maxPathSumUtil(root.left, res) 
	    rs = self.maxPathSumUtil(root.right, res) 
	  
	    # If both left and right children exist 
	    if root.left is not None and root.right is not None: 
	  
	        # update result if needed 
	        res[0] = max(res[0], ls + rs + root.data) 
	  
	        # Return maximum possible value for root being  
	        # on one side 
	        return max(ls, rs) + root.data 
	          
	    # If any of the two children is empty, return 
	    # root sum for root being on one side 
	    if root.left is None: 
	        return rs + root.data 
	    else: 
	        return ls + root.data
  
	# The main function which returns sum of the maximum  
	# sum path betwee ntwo leaves. THis function mainly  
	# uses maxPathSumUtil() 
	def maxPathSum(self): 
		res = [-sys.maxsize-1] 
		self.maxPathSumUtil(self.root, res)
		return res[0]


tree = BinarySearchTree()
tree.insert(8)
tree.insert(5) 
tree.insert(2) 
tree.insert(3)
tree.insert(7) 
tree.insert(11)
tree.insert(4)
print(tree.findDeadEnd(tree.root, -sys.maxsize-1, sys.maxsize))
print(tree.maxPathSum())
