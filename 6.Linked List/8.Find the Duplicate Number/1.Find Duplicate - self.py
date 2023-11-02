#!/usr/bin/env python3

def findDuplicate(nums: list[int]) -> int:
	occurr = [0] * (max(nums)+1)

	for i in nums:
		if not occurr[i]: occurr[i] = 1
		else: return i
		
	return nums[0]

nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))