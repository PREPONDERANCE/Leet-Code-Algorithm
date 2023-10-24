#!/usr/bin/env python3

def trapwater(height):
	water = 0
	l, r = 0, len(height)-1
	while l < len(height) and not height[l]: l += 1
	while r >= 0 and not height[r]: r -= 1
	
	if l > r: return water
	
	Left, Right = height[l], height[r]
	while l < r:
		if height[r] > height[l]:
			if height[r] > Right: Right = height[r]
			if height[l] > Left: Left = height[l]
			l += 1
			if not l == r:
				water += max(Left-height[l], 0)
		elif height[r] < height[l]:
			if height[l] > Left: Left = height[l]
			if height[r] > Right: Right = height[r]
			r -= 1
			if not l == r:
				water += max(Right-height[r], 0)
		else:
			Left = max(height[l], Left)
			Right = max(height[r], Right)
			l += 1
			r -= 1
			if l >= r: return water
			if l == r: water += Right-height[r]
			else:
				water += max(Right-height[r], 0)
				water += max(Left-height[l], 0)
				
	return max(water, 0)


height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
height = [5,5,1,7,1,1,5,2,7,6]
#height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [2, 0, 2]
#height = [2,1,0,2]
height = [7,9,7,3]
height = [8,2,8,9,0,1,7,7,9]
height = [8,5,1,1,7,3,2,1,5,8,3]
height = [7,5,7,8,7,6,5,0,7,1,4]

print(trapwater(height))