#!/usr/bin/env python3

def binarySearch(nums, l, r, target):
	if l <= r:
		m = (r+l)//2
		if nums[m] == target: return m
		elif nums[m] < target: return binarySearch(nums, m+1, r, target)
		return binarySearch(nums, l, m-1, target)
	
	return -1

nums = [1, 2, 3, 5, 7, 9, 10, 14, 19]
print(binarySearch(nums, 0, len(nums)-1, 19))