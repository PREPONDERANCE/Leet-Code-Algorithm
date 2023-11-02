#!/usr/bin/env python3

class Node:
	def __init__(self, x):
		self.val = x
		self.next = None
		self.random = None

def copyRandomList(head):
	if head == None: return None
	copy = {}
	
	curr = head
	while curr:
		copy[curr] = Node(curr.val)
		curr = curr.next
		
	curr = head
	while curr:
		copy[curr].next = copy.get(curr.next)
		copy[curr].random = copy.get(curr.random)
		curr = curr.next
	
	return copy[head]