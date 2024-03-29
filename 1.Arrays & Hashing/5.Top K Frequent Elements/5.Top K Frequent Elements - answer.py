#!/usr/bin/env python3

def topKFrequent(nums: list[int], k: int):
	count = {}
	freq = [[] for i in range(len(nums)+1)]
	
	for n in nums:
		count[n] = count.get(n, 0) + 1
	for Num, Freq in count.items():
		freq[Freq].append(Num)
	
	target = []
	for i in range(len(freq)-1, 0, -1):
		for num in freq[i]:
			target.append(num)
			if len(target) == k:
				return target
	
nums = [1]
print(topKFrequent(nums, 1))