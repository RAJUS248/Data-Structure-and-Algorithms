def removeDuplicates(nums):
    
    if not nums:
        return 0
    
    j = 1

    for i in range(1,len(nums)):

        if nums[i-1] != nums[i]:
            
            nums[j] = nums[i] 
            j += 1

    return nums,j

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))