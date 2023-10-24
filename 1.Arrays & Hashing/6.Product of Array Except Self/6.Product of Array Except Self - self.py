#!/usr/bin/env python3
def product(nums: list[int]):
	prefix, postfix = [1]*len(nums), [1]*len(nums)
	
	for i in range(1, len(nums)):
		prefix[i] = nums[i-1] * prefix[i-1]
		postfix[len(nums)-i-1] = postfix[len(nums)-i] * nums[len(nums)-i]
	
		arr = []
		for i in range(len(nums)):
			arr.append(prefix[i] * postfix[i])
	
			return arr