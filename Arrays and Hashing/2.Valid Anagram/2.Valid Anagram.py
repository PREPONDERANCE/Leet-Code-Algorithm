#!/usr/bin/env python3

def isAnagram(s: str, t: str) -> bool:
#		dict1, dict2 = {}, {}
#		for char1 in s:
#			dict1[char1] = dict1.get(char1, 0) + 1
#		for char2 in t:
#			dict2[char2] = dict2.get(char2, 0) + 1
#			
#		if len(dict1.items()) > len(dict2.items()):
#			bigger = dict1
#			smaller = dict2
#		else:
#			bigger = dict2
#			smaller = dict1
#				
#				
#		for c in bigger:
#			print(c)
#		for item in bigger.items():
#			if item[0] not in smaller.keys() or item[1] != smaller[item[0]]:
#				return False
#		
#		return True
	
	if len(s) != len(t): return False
	
	countS, countT = {}, {}
	for i in range(len(s)):
		countS[s[i]] = countS.get(s[i], 0) + 1
		countT[t[i]] = countT.get(t[i], 0) + 1
		
	for key in countS:
		if countS[key] != countT.get(key, 0):
			return False
	return True
	
	

string1 = "a"
string2 = "ab"

print(isAnagram(string1, string2))