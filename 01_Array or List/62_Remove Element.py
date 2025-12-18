def removeElement(nums, val):
    
    k = 0

    for i in range(len(nums)):

        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k,nums

nums = [3,3,2,2,3]
val = 3
print(removeElement(nums,val))



# def removeElement(nums, val):
    
#     count = 0
#     for num in nums:
#         if num == val:
#             count += 1

#     return len(nums) - count

# nums = [3,3,2,2,3]
# val = 3
# print(removeElement(nums,val))