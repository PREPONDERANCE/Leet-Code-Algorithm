#!/usr/bin/env python3

import collections
from collections import *

def majorityElement(nums):
	count = defaultdict(int)
	res = []
	
	for n in nums:
		count[n] += 1
		if len(count) <= 2: continue
		
		new_count = defaultdict(int)
		for n, v in count.items():
			if v > 1:
				new_count[n] = v-1
		count = new_count
		
	for n in count.keys():
		if nums.count(n) > len(nums) // 3:
			res.append(n)
			
	return res
	
print(majorityElement([3,2]))