#!/usr/bin/env python3
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
	res = defaultdict(list)
	for s in strs:
		count = [0] * 26
		for c in s:
			count[ord(c) - ord("a")] += 1
		res[tuple(count)].append(s)	
		
	return res.values()

strings = ["c", "c"]
print(groupAnagrams(strings))

# defaultdict specify the default value the dictionary holds
# With this precondition, we can manipulate dictionary just like what we did in C++
# where we directly write hashmap[key] = value without caring much about KeyError.

# collections.defaultdict is particularly useful when counting occurrences of items or grouping items by some criterion.