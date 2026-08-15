def findMaxConsecutiveOnes(nums):
        
        maxi = 0
        count = 0

        for num in nums:

            if num == 1:
                count += 1
                maxi = max(maxi,count)

            else:
                count = 0

        return maxi

nums = [1,1,0,1,1,1]
# print(findMaxConsecutiveOnes(nums))

def subarraySum(nums, k):

        count = 0
        cur_sum = 0
        seen = {0:1}

        for num in nums:
            
            cur_sum += num
            need = cur_sum - k

            if need in seen:
                count += seen[need]

            if cur_sum in seen:
                seen[cur_sum] += 1

            else: 
                seen[cur_sum] = 1

        return count

nums = [1,1,1]
k = 2
print(subarraySum(nums,k))