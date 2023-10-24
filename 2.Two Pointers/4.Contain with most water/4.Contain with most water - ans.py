#!/usr/bin/env python3

def containMostWater(height):
	l, r = 0, len(height)-1
	water = 0
	
	while l < r:
		water = max(water, (r-l)*min(height[l], height[r]))
		
		if height[l] > height[r]: r -= 1
		else: l += 1
	
	return water