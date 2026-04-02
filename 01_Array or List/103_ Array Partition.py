def arrayPairSum(nums):

    nums.sort()

    max_sum = 0
    
    # return sum(nums[::2])
    for i in range(0,len(nums),2):
        
        max_sum += nums[i]

    return max_sum 
  
nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))  
  
        
