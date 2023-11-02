#!/usr/bin/env python3

def precedence(char):
	if char == '*' or char == '/':
		return 2
	if char == '+' or char == '-':
		return 1
	return 0

def calculate(op1, optr, op2):
	if optr == '*': return op1 * op2
	if optr == '/': return int(float(op1) / op2)
	if optr == '+': return op1 + op2
	if optr == '-': return op1 - op2
	return -np.inf

def evalRPN(tokens):
	"""
	:type tokens: List[str]
	:rtype: int
	"""
	
	stack = []
	for token in tokens:
		if token[0].isdigit() or (len(token) > 1 and token[0] == '-'):
			stack.append(int(token))
		else:
			op2 = stack.pop()
			op1 = stack.pop()
			stack.append(calculate(op1, token, op2))
			
	return stack[-1]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))