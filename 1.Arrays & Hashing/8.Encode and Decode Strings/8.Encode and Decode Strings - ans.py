##!/usr/bin/env python3
#
#from collections import *
#
#def containsDuplicate(nums: list[int]) -> bool:
#	hashSet = set()
#	for n in nums:
#		if n in hashSet: return True
#		hashSet.add(n)
#	
#	return False
#
#def ValidAnagram(s: str, t: str) -> bool:
##	return Counter(s) == Counter(t)
#	
#	if len(s) != len(t): return False
#	countS, countT = {}, {}
#	
#	for i in range(s):
#		countS[s[i]] = countS.get(s[i], 0) + 1
#		countT[t[i]] = countT.get(t[i], 0) + 1
#		
#	for item in countS:
#		if countS[item] != countT.get(item, 0):
#			return False
#	return True
#
#def twoSum(nums: list[int], target: int) -> list[int]:
#	hashMap, arr = {}, []
#	
#	for i in range(len(nums)):
#		if target-nums[i] not in hashMap:
#			hashMap.update(nums[i], i)
#		else:
#			arr.append(hashMap[target-nums[i]])
#			arr.append(i)
#			return arr
#	
#
#def groupAnagram(strs: list[str]) -> list[list[str]]:
#	hashMap = defaultdict(list)
#	
#	for string in strs:
#		arr = [0] * 26
#		for char in string:
#			arr[ord(chr) - ord('a')] += 1
#		hashMap[tuple(arr)].append(string)
#	
#	return hashMap.values()
#
#
#def TopKFrequentElement(nums: list[int], k: int):
#	arr = [[] for i in range(len(nums) + 1)]
#	hashMap = {}
#	
#	for n in nums:
#		hashMap[n] = hashMap.get(n, 0) + 1
#	for key, value in hashMap.items():
#		arr[value].append(key)
#		
#	target = []	
#	for i in range(len(nums), -1, -1):
#		for num in arr[i]:
#			if len(target) == k: return target
#			target.append(num)
#	
#
#def productOfArrayExceptSelf(nums: list[int]):
#	arr = [1]*len(nums)
#	prefix, postfix = 1, 1
#	
#	for i in range(len(nums)):
#		arr[i] *= prefix
#		arr[len(nums)-1-i] *= postfix
#		prefix *= nums[i]
#		postfix *= nums[len(nums)-i-1]
#
#def isValidSudoku(board: list[list[str]]) -> bool:
#	rows = defaultdict(set)
#	cols = defaultdict(set)
#	squares = defaultdict(set)
#	
#	for r in range(0, 9, 3):
#		for c in range(0, 9, 3):
#			if board[r][c] == '.': continue
#			if (board[r][c] in rows[r] or
#				board[r][c] in cols[c] or
#				board[r][c] in squares[(r//3, c//3)]):
#				return False
#			
#			rows[r].add(board[r][c])
#			cols[c].add(board[r][c])
#			squares[(r//3, c//3)].add(board[r][c])
#		
#	return True


def encode(strs):
	string = ""
	for s in strs:
		string += (str(len(s)) + "#" + s)
	return string

def decode(strs):
	arr, i= [], 0
	
	while i < len(strs):
		j = i
		while strs[j] != '#':
			j += 1
		length = int(strs[i:j])
		i = j+1
		arr.append(strs[i:i+length])
		i += length
		
	return arr
	
print(encode(["123", "456", "890101010"]))
print(decode(encode(["123", "456", "890101010"])))