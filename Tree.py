class node:
	def __init__(self,data,children = []):
		self.parent = 0
		self.data = data
		self.children = children
		self.parentize()
		self.l = self.level()

	def level(self, lvl = 0):
		if self.parent is type(self):
			lvl += self.parent.level(lvl + 1)
		return lvl 

	def parentize(self):
		for child in self.children:
			if child:
				child.parent = self
		
	def __repr__(self, level = 0):
		ret = "\t"*level + repr(self.data) + "\n"
		for child in self.children:
			if child:
				ret += child.__repr__(level + 1)
		return ret



tree = node(1,[node(2,[node(5),node(2)]),node(1)])

print tree.children[0].children[1].l