def minSubArrayLen(target, nums):

        mini = float('inf')

        cur_sum = 0

        l = 0

        for r in range(len(nums)):  
    
            cur_sum += nums[r]  

            while cur_sum >= target:
                mini = min(mini,r - l + 1 )
                cur_sum -= nums[l]
                l += 1

        return 0 if mini == float('inf') else mini

target = 15
nums = [1,2,3,4,5] #[1,2,3,4,5] # [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))
