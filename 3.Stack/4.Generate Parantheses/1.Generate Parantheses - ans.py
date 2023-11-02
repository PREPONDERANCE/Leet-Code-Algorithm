#!/usr/bin/env python3

def generateParanthesis(n):
	stack, res = [], []
	open, close = 0, 0
	
	def generateUtil(open, close):
		if open == n and close == n:
			res.append(''.join(stack))
			return
		
		if open < n:
			stack.append('(')
			generateUtil(open+1, close)
			stack.pop()
	
		if close < open:
			stack.append(')')
			generateUtil(open, close+1)
			stack.pop()
	
	generateUtil(open, close)
	
	return res

print(generateParanthesis(3))