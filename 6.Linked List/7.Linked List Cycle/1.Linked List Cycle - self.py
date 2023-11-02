#!/usr/bin/env python3

class ListNode:
	def __init__(self, x, next=None):
		self.val = x
		self.next = None

class Solution:
	def hasCycle(self, head) -> bool:
		# Use a set to record every occurrence of node
		# return True if a node appears more than once
		hashSet = set()
		
		while head:
			if head not in hashSet:
				hashSet.add(head)
			else: return True
			head = head.next
		
		return False
	

testlist = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
head = ListNode(0)
tail = head

for i in testlist:
	temp = ListNode(i)
	tail.next = temp
	tail = tail.next
	
obj = Solution()
print(obj.hasCycle(head))