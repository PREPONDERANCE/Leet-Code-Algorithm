#!/usr/bin/env python3

def search(nums: list[int], target: int) -> int:
	l, r = 0, len(nums)-1

	def findMin(l, r):
		while l <= r:
			m = (l+r) // 2
			if nums[m-1] > nums[m]: return m
			elif nums[m] > nums[-1]: l = m+1
			else: r = m-1
			
		return m

	minElem = findMin(l, r)

	def bsearch(l, r):
		while l <= r:
			m = (l+r) // 2
			if nums[m] == target: return m
			elif nums[m] < target: l = m+1
			else: r = m-1
		return -1

	return max(bsearch(0, minElem-1), bsearch(minElem, len(nums)-1))

nums = [4,5,6,7,0,1,2]
target = 3

nums = [1]
target = 1

print(search(nums, target))