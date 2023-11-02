#!/usr/bin/env python3

# mid of two array

import numpy as np

def findMedianSortedArrays(nums1, nums2):
	A, B = nums1, nums2
	total = len(nums1) + len(nums2)
	half = total // 2
	
	if len(nums1) > len(nums2):
		A, B = B, A
	
	l, r = 0, len(A)-1
	while True:
		mid1 = (l+r)//2
		mid2 = half-mid1-2
		
		Aleft = A[mid1] if mid1 >= 0 else -np.inf
		Aright = A[mid1+1] if (mid1+1) < len(A) else np.inf
		Bleft = B[mid2] if mid2 >= 0 else -np.inf
		Bright = B[mid2+1] if (mid2+1) < len(B) else np.inf

		if Aleft <= Bright and Bleft <= Aright:
			if total % 2: return min(Aright, Bright)
			else: return ( max(Aleft, Bleft) + min(Aright, Bright) ) / 2
		elif Aleft <= Bright and Bleft > Aright:
			l = mid1+1
		else: r = mid1-1
		
	return -1

numList1 = [1, 3]
numList2 = [2]
print(findMedianSortedArrays(numList1, numList2))


# A cheating method

import statistics

def cheatCode(nums1, nums2):
	res = nums1 + nums2
	return statistics.mean(res)

print(cheatCode(numList1, numList2))