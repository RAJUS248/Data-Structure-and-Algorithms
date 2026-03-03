def maxProduct(nums):

    cur_max = nums[0]
    cur_min = nums[0]
    result = nums[0]

    for i in range(1,len(nums)):

        if nums[i] < 0:
            cur_max,cur_min = cur_min,cur_max

        cur_max = max(nums[i],cur_max * nums[i])
        cur_min = min(nums[i],cur_min * nums[i])

        result = max(result,cur_max)

    return result
       
nums = [0,2]

print(maxProduct(nums))



def maxProduct_v2(nums):

    n = len(nums)
    left_to_right = 1
    right_to_left = 1
    res = float('-inf')

    for i in range(n):

        if left_to_right == 0:
            left_to_right = 1

        if right_to_left == 0:
            right_to_left = 1
            
        left_to_right *= nums[i]
        right_to_left *= nums[n-i-1]
        
        res = max(res,left_to_right,right_to_left)

    return res
       
nums = [0,2]

print(maxProduct_v2(nums))



        # if len(nums) == 1:
        #     return nums[0]
        
        # maxi = float('-inf')
        # product = 1

        # for i in range(len(nums)):
            
        #     maxi = max(maxi,nums[i])

        #     if nums[i] != 0:
        #         product *= nums[i]
        #         maxi = max(maxi,product)

        # for i in range(len(nums)):
            
        #     if nums[i] == 0:
        #         break

        #     maxi = max(maxi,product)
        #     product = product // nums[i]

        # return maxi
