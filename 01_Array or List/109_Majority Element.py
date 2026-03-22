def majorityElement(nums):
        
    nums.sort()
    n =  len(nums)
    return nums[n//2]

def majorityElement_v2(nums2):

    candidate = None
    count = 0

    for num in nums2:

        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        
        else:
            count -= 1

    return candidate
        
nums = [2,2,1,1,1,2,2] # [3,2,3]
nums2 = [2,2,1,1,1,2,2]
print(majorityElement(nums))
print(majorityElement_v2(nums2))