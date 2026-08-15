def longestConsecutive(nums):
        
    nums.sort()
    
    l = 0
    length = 1
    maxi = 0
    for r in range(1,len(nums)):

        if nums[l] + 1 == nums[r]:

            length += 1
            l += 1

        elif nums[l] == nums[r]:
            l += 1
        
        else:
            maxi = max(maxi,length)
            length = 1
            l += 1

    maxi = max(maxi,length) 
    return maxi

def longestConsecutive_v2(nums):

        seen = set(nums)

        maxi = 0

        for num in seen:

            if num - 1 not in seen:  
                cur = num
                length = 0

                while cur in seen:

                    length += 1
                    cur = cur + 1

                maxi = max(maxi,length)
                
        return maxi
        
nums = [1,2,6,7,8] # [0,3,7,2,5,8,4,6,0,1] # [100,4,200,1,3,2] #
print(longestConsecutive(nums))
print(longestConsecutive_v2(nums))


