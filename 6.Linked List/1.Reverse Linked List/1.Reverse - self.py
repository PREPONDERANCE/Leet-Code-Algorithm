#!/usr/bin/env python3

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
class Solution:
	def reverseList(self, head):
		if not head.next: return head
		temp = self.reverseList(head.next)
		head.next.next = head
		head.next = None
		return temp
	
a = ListNode(2)
b = ListNode(3, a)
c = ListNode(4, b)

obj = Solution()
c = obj.reverseList(c)

while c:
	print(c.val)
	c = c.next