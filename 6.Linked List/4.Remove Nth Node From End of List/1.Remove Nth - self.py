#!/usr/bin/env python3

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
	def add(self, head, val):
		temp = ListNode(val, head)
		return temp
		
class Solution:
	def removeNthFromEnd(self, head, n: int):
		# fast-slow pointer to determine the pos
		fast, slow, prev = head, head, None
		
		for i in range(n):
			fast = fast.next
			
		while fast:
			prev = slow
			fast = fast.next
			slow = slow.next
			
		if not prev: return head.next
		prev.next = slow.next
		return head
	
head = ListNode(2)
head = head.add(head, 1)

obj = Solution()
obj.removeNthFromEnd(head, 1)

while head:
	print(head.val)
	head = head.next