def minSubArrayLen(target, nums):
        
        mini = float('inf')

        l = 0
        cur_sum = 0

        for r in range(len(nums)):

            cur_sum += nums[r]

            while cur_sum  >= target:
                mini = min(mini,r - l + 1)
                cur_sum -= nums[l]
                l += 1
                
        if mini ==  float('inf'):
             return 0
        
        return mini

target = 15
nums = [5,1,3,5,10,7,4,9,2,8] # [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))

arr = [1,2,3,4,5]
print(arr[-3:])