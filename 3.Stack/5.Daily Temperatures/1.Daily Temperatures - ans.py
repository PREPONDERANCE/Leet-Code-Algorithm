#!/usr/bin/env python3

def dailyTemperatures(temperatures):
	"""
	:type temperatures: List[int]
	:rtype: List[int]
	"""
	res = [0]*len(temperatures)
	stack = []

	for i in range(len(temperatures)):
		while stack and temperatures[i] > temperatures[stack[-1]]:
			res[stack[-1]] = i-stack[-1]
			stack.pop()
		stack.append(i)
		
	return res
			
print(dailyTemperatures([73,74,75,71,69,72,76,73]))