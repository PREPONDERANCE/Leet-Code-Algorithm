#!/usr/bin/env python3

def twoSum(nums: list[int], target: int) -> list[int]:
	i, j, arr = 0, len(nums)-1, []
	while i < j:
		if nums[i] + nums[j] > target:
			j -= 1
		elif nums[i] + nums[j] < target:
			i += 1
		else: return [i+1, j+1]
			
	return arr

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))