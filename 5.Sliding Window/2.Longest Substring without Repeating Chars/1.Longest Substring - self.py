#!/usr/bin/env python3

def lengthOfLongestSubstring(s: str) -> int:
	l, r = 0, 0
	maxL = 0

#	while l < len(s):
#		r = l
#		hashSet = set()
#		while r < len(s):
#			if s[r] not in hashSet:
#				hashSet.add(s[r])
#				r += 1
#			else: break
#		maxL = max(maxL, r-l)
#		l += 1
	
	while l < len(s):
		r = l
		hashMap = {}
		while r < len(s):
			if s[r] not in hashMap.keys():
				hashMap[s[r]] = hashMap.get(s[r], r)
				r += 1
			else: break
		maxL = max(maxL, r-l)
		if r >= len(s): l += 1
		else: l = hashMap[s[r]] + 1
		
	return maxL

string = ' '
#string = "abcabcbb"
#string = "bbbbb"
#string = "pwwkew"
#string = "dvdf"

print(lengthOfLongestSubstring(string))