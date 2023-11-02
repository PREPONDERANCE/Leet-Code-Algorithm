#!/usr/bin/env python3

def maxProfit(prices: list[int]) -> int:
	maxP, minP = 0, prices[0]

	for p in prices:
		if p < minP: minP = p
		else: maxP = max(maxP, p-minP)
		
	return maxP