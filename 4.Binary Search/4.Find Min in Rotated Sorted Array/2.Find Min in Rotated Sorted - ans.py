#!/usr/bin/env python3

def findMin(nums):
	l, r = 0, len(nums)-1
	res = nums[0]
	
	while l <= r:
		m = (l+r) // 2
		if nums[m] < res:
			res = nums[m]
			r = m-1
		else: l = m+1
	
	return res