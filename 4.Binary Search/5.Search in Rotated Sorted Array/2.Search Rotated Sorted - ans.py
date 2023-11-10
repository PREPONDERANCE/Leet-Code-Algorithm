#!/usr/bin/env python3

def search(nums: list[int], target: int) -> int:
	l, r = 0, len(nums)-1

	while l <= r:
		m = (l+r) // 2
		if target == nums[m]: return m
		
		# left portion of the array
		if nums[l] <= nums[m]:
			if target > nums[m] or target < nums[l]: l = m+1
			else: r = m-1
		else:
			if target < nums[m] or target > nums[r]: r = m-1
			else: l = m+1
	return -1
		
	
nums = [4,5,6,7,8,1,2,3]
target = 8

print(search(nums, target))