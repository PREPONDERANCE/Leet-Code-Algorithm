#!/usr/bin/env python3

def largestRectangle(heights):
#	maxArea = 0
#	
#	for i in range(len(heights)):
#		minH = heights[i]
#		for j in range(i+1, len(heights)):
#			minH = min(minH, heights[j])
#			maxArea = max(maxArea, (j-i+1)*minH)
#			
#	return maxArea
	stack, maxArea = [], 0
	
	for i, h in enumerate(heights):
		start = i
		while stack and stack[-1][1] > h:
			index, height = stack.pop()
			maxArea = max(maxArea, height*(i-index))
			start = index
		stack.append((start, h))
	
	for i, h in stack:
		maxArea = max(maxArea, h*(len(heights)-i))
	
	return maxArea

print(largestRectangle([2,1,2]))