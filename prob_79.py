from Tree import *
import random

class PKDTree(node):
	def __init__(self, data, children=[0,0]):
		node.__init__(self,data,children)

		with open("keylog.txt") as f:
			self.logs = set([line[:3] for line in f])
			#create set of logs
			self.keys = set([num for elem in self.logs for num in elem])
			#creates set of keys from logs

		self.orders = [[log[0:2],log[1:3],log[0:3:2]] for log in self.logs]
		#seperates logs into lists of orders
		self.orders = set([num for elem in self.orders for num in elem])
		#seperates list of orders into a set of relations
		
	def inorder(self):
		"""recursive algorithm to print inorder traversal of tree """
		ret = ""
		if self.children[0] or self.children[1]:
			#if the parent of the tree is not a leaf
			if self.children[0]:
				#if the left child exists add it to the return
				ret += self.children[0].inorder()
			ret += self.data
			#add the root to the return
			if self.children[1]:
				#if the right child exist add it to the return
				ret += self.children[1].inorder()
		else:
			#if it is a leaf add it to the return
			ret +=self.data
		return ret

	def less_than(self,xy):
		if xy in self.orders:
			#if the expression x<y is in the relation
			return True
		else:
			return False

	def add(self,key):
		if self.less_than(key+self.data):			
			if self.children[0]:
				#if it is less than call the function on the left child if it exist
				self.children[0].add(key)
			else:
				#if the left child does not exist a new PKDTree to the left side
				self.children = [PKDTree(key),self.children[1]]
		else:
			if self.children[1]:
				#if it is greater than call the function on the right child if it exist
				self.children[1].add(key)
			else:
				#if the right child does not exist a new PKDTree to the right side
				self.children = [self.children[0],PKDTree(key)]
	
	def PKD(self):
		self.keys = self.keys - set(self.data)
		for key in self.keys:
			self.add(key)

ay = PKDTree("0")
ay.PKD()

print(ay)
print(ay.inorder())