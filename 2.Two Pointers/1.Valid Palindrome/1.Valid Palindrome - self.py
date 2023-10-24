#!/usr/bin/env python3

def isPalindrome(s: str) -> bool:
	i, j = 0, len(s)-1
	while j-i >=1:
		if s[i].isalnum() and s[j].isalnum():
			if s[i].lower() == s[j].lower():
				i += 1
				j -= 1
			else:
				return False
		else:
			while i < len(s) and not s[i].isalnum(): i += 1
			while j >= 0 and not s[j].isalnum(): j -= 1
			
	if i > len(s) or j < 0: return False
	return True

print(isPalindrome(".,"))

