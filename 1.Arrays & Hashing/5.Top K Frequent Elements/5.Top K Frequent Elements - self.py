#!/usr/bin/env python3
from collections import defaultdict

def topKFrequent(nums: list[int], k: int):
	hashMap = defaultdict(int)
	
	for num in nums:
		hashMap[num] += 1
	
	sorted_dict_desc = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
	
	arr, target = [], []
	for key in sorted_dict_desc.keys():
		arr.append(key)

	for i in range(k):
		target.append(arr[i])
	
	return target
	
nums = [3, 0, 1, 0]
print(topKFrequent(nums, 1))