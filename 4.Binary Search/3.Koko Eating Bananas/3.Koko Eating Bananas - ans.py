import math

def minEatingSpeed(piles, h):
	l, r = 1, max(piles)
	res = r
	
	while l <= r:
		k = (l+r) // 2
		
		t = 0
		for p in piles:
			t += math.ceil(p / k)
		
		if t <= h:
			res = min(res, k)
			r = k-1
		else: l = k+1
		
	return res

piles = [312884470]
h = 312884469

print(minEatingSpeed(piles, h))