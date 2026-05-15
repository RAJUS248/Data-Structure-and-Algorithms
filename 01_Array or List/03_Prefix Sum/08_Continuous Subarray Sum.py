def checkSubarraySum(nums, k):
        
        n = len(nums)

        seen = {0:-1}

        pre_sum = 0

        for i in range(n):

            pre_sum += nums[i]

            rem = pre_sum % k

            if  rem not in seen:

                seen[rem] = i

            elif i - seen[rem] > 1:

                return True

        return False
        

nums = [23,2,4,6,6]
k = 7
print(checkSubarraySum(nums,k))
