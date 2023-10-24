#!/usr/bin/env python3

# Instead of comparing the value and updating the left and right boundary
# We can directly compare and left and right boundary

# O(n) memory

def trapWater(height):
	water = 0
	maxLeft, maxRight = [0]*len(height), [0]*len(height)
	
	for i in range(1, len(height)):
		maxLeft[i] = max(height[0:i])
		maxRight[len(height)-i-1] = max(height[len(height)-i-1:len(height)])
	
	maxBound = [min(maxRight[i], maxLeft[i]) for i in range(len(height))]
	
	for i in range(len(height)):
		water += max(maxBound[i]-height[i], 0)
	
	return water

# O(1) memory

#def trapWater(height):
#	l, r = 0, len(height)-1
#	water = 0
#	
#	maxLeft, maxRight = height[l], height[r]
#	while l < r:
#		if maxLeft < maxRight:
#			l += 1
#			maxLeft = max(maxLeft, height[l])
#			water += maxLeft-height[l]
#		else:
#			r -= 1
#			maxRight = max(maxRight, height[r])
#			water += maxRight-height[r]
#	
#	return water
	
height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
height = [5,5,1,7,1,1,5,2,7,6]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [2, 0, 2]
height = [2,1,0,2]
height = [7,9,7,3]
height = [8,2,8,9,0,1,7,7,9]
height = [8,5,1,1,7,3,2,1,5,8,3]
height = [7,5,7,8,7,6,5,0,7,1,4]
print(trapWater(height))