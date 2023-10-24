#!/usr/bin/env python3

def twoSum(numbers: list[int], target: int) -> list[int]:
	arr = []
	for i in range(len(numbers)):
		if target-numbers[i] in numbers[i+1::]:
			arr.append(i+1)
			arr.append(numbers[i+1::].index(target-numbers[i])+2+i)
			break
		
	return arr

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))