#!/usr/bin/env python3

def searchMatrix(matrix, target):
	
	def binarySearch(nums, l, r):
		if l <= r:
			m = (l+r) // 2
			if nums[m] == target: return m
			elif nums[m] < target: return binarySearch(nums, m+1, r)
			return binarySearch(nums, l, m-1)
		
		return r
	
	# Why would we return r here?
	# Either r denoting the line target falls in or it equals -1
	
	col = [matrix[i][0] for i in range(len(matrix))]
	rowNum = binarySearch(col, 0, len(col)-1)
	if rowNum < 0: return False
	
	row = [matrix[rowNum][i] for i in range(len(matrix[0]))]
	colNum = binarySearch(row, 0, len(row)-1)
	if colNum < 0: return False
	
	return matrix[rowNum][colNum] == target

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

matrix = [[1]]
target = 0

print(searchMatrix(matrix, target))