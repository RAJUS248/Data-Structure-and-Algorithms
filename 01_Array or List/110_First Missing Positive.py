def firstMissingPositive(nums):

    n = len(nums)

    for i in range(n): 

        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    for i in range(n):
        if nums[i] != i+1:
            return i+1

    return n+1

def firstMissingPositive_v2(nums):

    seen = set(nums)

    i = 1
    
    while i in seen:
        i += 1

    return i

nums = [3,4,-1,1]
print(firstMissingPositive(nums))
print(firstMissingPositive_v2(nums))