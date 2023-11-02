#!/usr/bin/env python3
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
class Solution:
	def llen(self, head):
		length = 0
		while head:
			length += 1
			head = head.next
		return length
	
	def addTwoNumbers(self, l1, l2):
		A, B, carry = l1, l2, 0
		if self.llen(l1) > self.llen(l2):
			A, B = B, A
		tail, add = B, B
			
		while A:
			tail = B
			total = A.val + B.val + carry
			carry = total // 10
			total %= 10
			
			B.val = total
			
			A = A.next
			B = B.next
			
		while B:
			tail = B
			B.val += carry
			carry = B.val // 10
			B.val %= 10
			
			B = B.next
			
		if carry:
			newNode = ListNode(carry)
			tail.next = newNode
			
		return add
	

obj = Solution()

a = ListNode(9)
b = ListNode(9,a)
c = ListNode(9,b)

e = ListNode(9)
f = ListNode(9,e)
g = ListNode(9,f)
h = ListNode(9,g)

a = obj.addTwoNumbers(c, h)
while a:
	print(a.val)
	a = a.next
