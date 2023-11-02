#!/usr/bin/env python3

def copyRandomList(head):
		# Establish an array recording the position each random pointer points to
		random = []
		static_head = head
	
		while head:
			if not head.random: random.append(100000)
			else:
				count, temp = 0, static_head
				while not temp == head.random:
					temp = temp.next
					count += 1
				random.append(count)
			head = head.next
			
		head, newHead = static_head, Node(0)
		merged = newHead
	
		while head:
			temp = Node(head.val)
			merged.next = temp
			merged = merged.next
			head = head.next
			
		merged = newHead.next
		for r in random:
			if r == 100000:
				merged.random = None
			else:
				temp = newHead.next
				count = 0
				while not count == r:
					count += 1
					temp = temp.next
				merged.random = temp
			merged = merged.next
			
		return newHead.next