def product(nums: list[int]):
    prefix, postfix, arr = 1, 1, [1] * len(nums)
    
    for i in range(0, len(nums)):
        arr[i] *= prefix
        arr[len(nums)-i-1] *= postfix
        prefix *= nums[i]
        postfix *= nums[len(nums)-i-1]
                
    return arr
        
ints = [1, 2, 3, 4]
print(product(ints))