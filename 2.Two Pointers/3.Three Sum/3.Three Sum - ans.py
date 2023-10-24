def threeSum(nums: list[int]) -> list[list[int]]:

    nums = sorted(nums)
    i, j, k, arr = 0, 0, 0, []

    while i <= len(nums)-3:
        if i-1 >= 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        j, k = i+1, len(nums)-1
        while j < k:
            if nums[j] + nums[k] + nums[i] < 0: j += 1
            elif nums[j] + nums[k] + nums[i] > 0: k -= 1
            else:
                arr.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
        i += 1
        
    return arr
        
        
numList = [-2, -2, 0, 0, 2, 2]
print(threeSum(numList))