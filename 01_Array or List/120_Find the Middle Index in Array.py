def findMiddleIndex(nums):
        
        left = []
        left_sum = 0


        for num in nums:
            left_sum += num
            left.append(left_sum)
        
        right = []
        right_sum = 0

        for i in range(len(nums)-1,-1,-1):
            right_sum += nums[i]
            right.append(right_sum)

        right = right[::-1]
       
        for i in range(len(nums)):
             
            if left[i] - nums[i] == right[i] - nums[i]:
                return i
            
        return -1

nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))


def findMiddleIndex_v2(nums):
        
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]

        return -1

nums = [2,3,-1,8,4]
print(findMiddleIndex_v2(nums))


def findMiddleIndex_v3(nums):
        
        right_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
            

        return -1

nums = [2,3,-1,8,4]
print(findMiddleIndex_v3(nums))