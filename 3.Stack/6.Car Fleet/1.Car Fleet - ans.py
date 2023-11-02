#!/usr/bin/env python3

def carFleet(target, position, speed):
	stack = []
	for p, s in sorted(zip(position, speed))[::-1]:
		dis = target-p
		if not stack: stack.append(dis / s)
		elif dis / s > stack[-1]: stack.append(dis / s)
	return len(stack)

position = [6, 8]
speed = [3, 2]
target = 10

print(carFleet(target, position, speed))