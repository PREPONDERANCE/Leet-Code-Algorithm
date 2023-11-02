#!/usr/bin/env python3

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
class Solution:
	def reverse(self, head):
		if not head or not head.next: return head
		temp = self.reverse(head.next)
		head.next.next = head
		head.next = None
		return temp
	
	def reorderList(self, head) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""
		fast, slow = head, head
		while fast.next:
			fast = fast.next
			if fast.next:
				slow = slow.next
				fast = fast.next
				
		head1, head2 = head, slow.next
		slow.next = None
		head2 = self.reverse(head2)
		
		L = ListNode(0)
		merged = L
		i = 1
		
		while head1 and head2:
			if i % 2:
				L.next = head1
				head1 = head1.next
			else:
				L.next = head2
				head2 = head2.next
			L = L.next
			i += 1
		
		L.next = head1 if head1 else head2
		head = merged.next
		
obj = Solution()
a = ListNode(4)
b = ListNode(3,a)
c = ListNode(2,b)
d = ListNode(1,c)

obj.reorderList(d)
while d:
	print(d.val)
	d = d.next