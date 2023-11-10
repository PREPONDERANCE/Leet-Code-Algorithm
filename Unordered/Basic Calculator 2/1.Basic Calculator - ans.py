##!/usr/bin/env python3
#
## This Solution takes O(n) time and space complexity
#def perform(op1, cal, op2):
#	if cal == '*': return op1 * op2
#	if cal == '/': return op1 // op2
#	if cal == '+': return op1 + op2
#	if cal == '-': return op1 - op2
#
#def precedence(op):
#	if op == '*' or op == '/': return 2
#	if op == '+' or op == '-': return 1
#	return 0
#
#def isoptr(c):
#	return c == '+' or c == '-' or c == '*' or c == '/' or c == '(' or c == ')' or c == '='
#
#def EvaluateInfix(s: str):
#	i, j, opnd, optr = 0, 0, [], []
#	
#	while s[i] != '=':
#		while not isoptr(s[j]): j += 1
#		if s[i].isdigit() or s[i] == '.':
#			opnd.append(float(s[i:j]))
#		else:
#			j += 1
#			if s[i] == '(': optr.append(s[i])
#			elif s[i] == ')':
#				while len(optr) and optr[-1] != '(':
#					op2 = opnd.pop()
#					op1 = opnd.pop()
#					opnd.append(perform(op1, optr.pop(), op2))
#				optr.pop()
#			elif not len(optr) or precedence(s[i]) - precedence(optr[-1]) > 0:
#				optr.append(s[i])
#			elif precedence(s[i]) - precedence(optr[-1]) <= 0:
#				op2 = opnd.pop()
#				op1 = opnd.pop()
#				opnd.append(perform(op1, optr.pop(), op2))
#				optr.append(s[i])
#		i = j
#		
#	while len(optr):
#		op2 = opnd.pop()
#		op1 = opnd.pop()
#		opnd.append(perform(op1, optr.pop(), op2))
#		
#	return opnd.pop()


# This solution takse O(n) time and O(1) space
def calculate(s: str):
	res, curr, prev, optr = 0, 0, 0, '+'
	i = 0
	
	while i < len(s):
		if s[i] == ' ':
			i += 1
			continue
		elif s[i].isdigit():
			j = i+1
			while j < len(s) and s[j].isdigit():
				j += 1
			curr = int(s[i:j])
			i = j-1
		
			if optr == '+':
				res += curr
				prev = curr
			elif optr == '-':
				res -= curr
				prev = -curr
			elif optr == '*':
				res -= prev
				res += prev * curr
				prev = prev * curr
			elif optr == '/':
				res -= prev
				res += int(prev / curr)
				prev = int(prev / curr)
		else: optr = s[i]
		i += 1
	
	return res

print(calculate("1*2-3/4+5*6-7*8+9/10"))