def findUnsortedSubarray(nums):

    n = len(nums)
    max_num = nums[0]
    min_num = nums[-1]

    start = 0
    end = -1
    
    for i in range(1,n):
        max_num = max(max_num,nums[i])

        if nums[i] < max_num:
            end = i

    for i in range(n-2,-1,-1):
        min_num = min(min_num,nums[i])

        if nums[i] > min_num:
            start = i

    return end - start + 1

nums = [2,6,4,8,10,9,15]
print(findUnsortedSubarray(nums))