def pivotIndex(nums):

        left = 0
        right = sum(nums)  
    
        for pivot in range(len(nums)):
            right -= nums[pivot]
            if left == right:
                return pivot

            else:
                left += nums[pivot]

        return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))
