#!/usr/bin/env python3

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	head = ListNode(0)
	merged = head

	while list1 and list2:
		if list1.val < list2.val:
			head.next = list1
			list1 = list1.next
		else:
			head.next = list2
			list2 = list2.next
		head = head.next
		
	head.next = list1 if list1 and not list2 else list2

	return merged.next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
	if len(lists) == 0: return None
	if len(lists) == 1: return lists[0]
	
	for j in range(len(lists)-1, 0, -1):
		lists[0] = self.mergeTwoLists(lists[0], lists[j]) 
		
	return lists[0]