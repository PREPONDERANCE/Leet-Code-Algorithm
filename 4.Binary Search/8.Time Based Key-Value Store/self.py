#!/usr/bin/env python3

import collections
from collections import defaultdict

class timeMap(object):
	def __init__(self):
		self.map = defaultdict(list[tuple])
	
	def set(self, key: str, value: str, timestamp: int) -> None:
		self.map[key].append((value, timestamp))
		
	def get(self, key: str, timestamp: int) -> str:
		series = self.map[key]
		if series == []: return ""
		
		l, r = 0, len(series)-1
		while l <= r:
			m = (l+r) // 2
			if series[m][1] == timestamp: return series[m][0]
			elif series[m][1] < timestamp: l = m+1
			else: r = m-1
		
		if r < 0: return ""
		return series[r][0]
		

time = timeMap()
#time.set("foo", "bar", 1)
#print(time.get("foo", 3))
#time.set("foo", "bar2", 4)
#print(time.get("foo", 4))
#print(time.get("foo", 5))

time.set("love","high",10)
time.set("love","low",20)
print(time.get("love",5))
print(time.get("love",10))
print(time.get("love",15))
print(time.get("love",20))
print(time.get("love",25))