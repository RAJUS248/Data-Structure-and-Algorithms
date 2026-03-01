def maximumProduct(nums):
        
        nums.sort()
        n = len(nums)

        max_product1 = nums[-1] * nums[-2] * nums[-3]

        max_product2 = nums[0] * nums[1] * nums[-1]

        return max(max_product1,max_product2)

nums = [-1,-2,-3]
print(maximumProduct(nums))


            # if n < 3:
        #     return 0

        # max_product = 1
        # count = 3

        # for i in range(n-1,-1,-1):

        #     if count != 0:
        #         max_product *= nums[i]
        #         count -= 1

        #     if count == 0:
        #         return max_product