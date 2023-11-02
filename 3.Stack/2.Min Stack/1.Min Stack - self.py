#!/usr/bin/env python3

class MinStack(object):
	
	def __init__(self):
		self.stack = []
		self.minElem = []
		
	def push(self, val):
		"""
		:type val: int
		:rtype: None
		"""
		self.stack.append(val)
		
		if not self.minElem:
			self.minElem.append(val)
			return
		
		curr_min = self.minElem[-1]
		if curr_min > val: self.minElem.append(val)
		else: self.minElem.append(curr_min)
		
	def pop(self):
		"""
		:rtype: None
		"""
		if not self.stack: return
		self.stack.pop()
		self.minElem.pop()
		
	def top(self):
		"""
		:rtype: int
		"""
		if not self.stack: return -np.inf
		return self.stack[-1]
	
	def getMin(self):
		"""
		:rtype: int
		"""
		return self.minElem[-1]
	
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())
obj.pop()
print(obj.top())
