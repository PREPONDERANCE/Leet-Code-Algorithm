#!/usr/bin/env python3

def twoSum(nums: list[int], target: int) -> list[int]:
#	list_sort = sorted(nums)
#	target_list = []
#	
#	for i in list_sort:
#		if target-i in list_sort:
#			target_list.append(nums.index(i))
#			nums[nums.index(i)] = target-i+1
#			try:
#				target_list.append(nums.index(target-i))
#			except ValueError:
#				continue
#			nums[nums.index(i)] = target-i-1
#			return target_list

	
#	The solution above takes O(nlogn) time
	
#	We can use hashmap to solve this problem in O(n) time
	
	hashMap, target_arr = {}, []
	
	for i in range(len(nums)):
		if target-nums[i] not in hashMap:
			hashMap[nums[i]] = hashMap.get(nums[i], 0) + i
		else:
			target_arr.append(hashMap[target-nums[i]])
			target_arr.append(i)
			return target_arr
			
input_array = [2, 1, 5, 3]
target = 4;

print(twoSum(input_array, target))