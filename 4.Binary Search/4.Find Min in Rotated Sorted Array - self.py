def findMin(nums):
	l, r = 0, len(nums)-1
	
	while l <= r:
		m = (l+r) // 2
		if nums[m-1] > nums[m]: return nums[m]
		elif nums[m] < nums[-1]: r = m-1
		else: l = m+1
	
	return nums[r]

nums = [4,5,6,7,0,1,2]
nums = [3,4,5,1,2]
nums = [11,13,15,17]
nums = [1]
#nums = [6,7,1,2,3,4]

print(findMin(nums))