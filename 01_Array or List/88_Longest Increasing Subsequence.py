def longest_of_LIS(nums):
    n = len(nums)
    
    LIS = [1] * n

    for i in range(1,n):
        for j in range(i):

            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i],LIS[j]+1)

    return max(LIS),LIS

nums = [10,9,2,5,3,7,101,18]
print(longest_of_LIS(nums))