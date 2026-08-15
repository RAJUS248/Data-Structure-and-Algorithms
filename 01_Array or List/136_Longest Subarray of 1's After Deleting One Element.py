def longestSubarray(nums):
        
    maxi = 0
    zero_idx = -1
    
    l = 0
    r = 0


    while r < len(nums):

        if nums[r] == 0:
            l = zero_idx + 1
            zero_idx = r

        maxi = max(maxi, r - l)
        r += 1

    return maxi

    

nums = [0,1,1,0,0,1,1,1,0,0]
print(longestSubarray(nums))