#!/usr/bin/env python3

def maxProfit(prices: list[int]) -> int:
	l, r = 0, 0
	maxP = 0
	
	while r < len(prices):
		p = prices[r]-prices[l]
		if p < 0: l += 1
		else:
			maxP = max(maxP, p)
			r += 1
			
	return maxP