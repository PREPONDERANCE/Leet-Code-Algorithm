#!/usr/bin/env python3

def singleNumber(nums: list(int)):
	x = 0
	for n in nums:
		x ^= n
	return x