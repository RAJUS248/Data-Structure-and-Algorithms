import bisect
def answerQueries(nums, queries):
        
        # res = []
        # nums.sort()
        # for num in queries:

        #     cur_sum = 0
        #     count = 0  

        #     for n in nums:

        #         cur_sum += n     

        #         if cur_sum <= num:
        #             count += 1

        #         else:
        #             cur_sum -= n

        #     res.append(count)

        # return res

        nums.sort()
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]

        res = []

        for q in queries:
            x = bisect.bisect(nums,q)
            res.append(x)

        return res

        # nums.sort()
        # for i in range(1,len(nums)):
        #     nums[i] = nums[i] + nums[i-1]

        # res = []
        # for q in queries:
            
        #     left = 0
        #     right = len(nums)-1
        #     count = 0

        #     while left <= right:
                 
        #         mid = (right + left)//2

        #         if nums[mid] <= q:
                    
        #             count = mid + 1
        #             left = mid + 1
                
        #         else:
        #             right = mid - 1

        #     res.append(count)
        
        # return res
nums = [469781,45635,628818,324948,343772,713803,452081]
queries = [816646,929491]
print(answerQueries(nums,queries))
