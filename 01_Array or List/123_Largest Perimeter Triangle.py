def largestPerimeter(nums):

    n = len(nums)
    nums.sort()
    
    for i in range(n-1,1,-1):
        if nums[i-2] + nums[i-1] > nums[i]:
            return nums[i] + nums[i-1] + nums[i-2]
            
    return 0

nums = [1,2,1,10] # [3,4,15,2,9,4] # [2,3,3,6] # [2,1,2] # [1,2,1,10]
print(largestPerimeter(nums))