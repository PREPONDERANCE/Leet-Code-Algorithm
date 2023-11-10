#!/usr/bin/env python3

class Node:
	def __init__(self, key, value):
		self.key, self.val = key, value
		self.prev = self.next = None
		
class LRUCache:
	
	def __init__(self, capacity: int):
		self.cap = capacity
		self.cache = {}
		
		self.left, self.right = Node(0, 0), Node(0, 0)
		self.left.next, self.right.prev = self.right, self.left
		
	def insert(self, node):
		node.next = self.right
		node.prev = self.right.prev
		node.prev.next = node
		self.right.prev = node
		
		
	def remove(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev
		
	def get(self, key: int) -> int:
		if key in self.cache:
			self.remove(self.cache[key])
			self.insert(self.cache[key])
			return self.cache[key].val
		return -1
	
	def put(self, key: int, value: int) -> None:
		if key in self.cache:
			self.remove(self.cache[key])
		self.cache[key] = Node(key, value)
		self.insert(self.cache[key])
		
		if len(self.cache) > self.cap:
			lru = self.left.next
			self.remove(lru)
			del self.cache[lru.key]
			
			
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)