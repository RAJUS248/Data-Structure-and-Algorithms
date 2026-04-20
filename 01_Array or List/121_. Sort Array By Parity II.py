def sortArrayByParityII(nums):
        
        n = len(nums)
        even = 0
        odd = 1

        while even < n and odd < n:
            
            if nums[even] % 2 == 0:
                even += 2

            elif nums[odd] % 2 != 0:
                odd += 2

            else:
                nums[even],nums[odd] = nums[odd],nums[even]

                even += 2
                odd += 2

        return nums
        
            
nums = [3,0,4,0,2,1,3,1,3,4]# [4,2,5,7] # [1,4,4,3,0,3]
print(sortArrayByParityII(nums))

        