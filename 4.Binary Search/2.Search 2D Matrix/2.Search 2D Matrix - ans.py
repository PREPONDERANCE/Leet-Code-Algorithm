#!/usr/bin/env python3

def searchMatrix(matrix, target):
	Rows, Cols = len(matrix), len(matrix[0])
	
	top, bot = 0, Rows-1
	while top <= bot:
		row = (top+bot) // 2
		if target > matrix[row][-1]:
			top = row+1
		elif target < matrix[row][0]:
			bot = row-1
		else: break
	
	if top > bot: return False
	
	l, r = 0, Cols-1
	while l <= r:
		m = (l+r) // 2
		if matrix[row][m] == target: return True
		elif matrix[row][m] < target:
			l = m+1
		else: r = m-1
	
	return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

matrix = [[1]]
target = 2

print(searchMatrix(matrix, target))