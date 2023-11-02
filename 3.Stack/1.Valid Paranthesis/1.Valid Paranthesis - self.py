#!/usr/bin/env python3

def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	openBrackets = "({["
	stack = []

	for c in s:
		if c in openBrackets:
			stack.append(c)
		else:
			if not stack: return False
			if ( c == ')' and stack[-1] == '(' or
				c == '}' and stack[-1] == '{' or
				c == ']' and stack[-1] == '[' ):
					stack.pop()
					continue
			else: return False
		
	if not stack: return True
	return False
