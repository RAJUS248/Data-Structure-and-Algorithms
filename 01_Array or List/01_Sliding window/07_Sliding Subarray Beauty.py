def getSubarrayBeauty(nums, k, x):
        
    res = []
    freq = [0] * 101
    
    def get_beauty():
        count = 0
        for i in range(0,50):
            count += freq[i]
            
            if count >= x:
                return i - 50
            
        return 0
    
    l = 0
    for r in range(len(nums)):

        freq[nums[r] + 50] += 1

        if r - l + 1 > k:
            freq[nums[l]+50] -= 1
            l += 1

        if r - l + 1 == k:
            res.append(get_beauty())
        
    return res

nums = [1,-1,-3,-2,3]
k = 3
x = 2
print(getSubarrayBeauty(nums,k,x))



#  res = []
#         beauty = deque()
#         l = 0
#         for r in range(len(nums)):

#             beauty.append(nums[r])

#             if r - l + 1 == k:
#                 temp = list(beauty)
#                 temp.sort()
#                 res.append(temp[x-1])
#                 l += 1
#                 beauty.popleft()

#         return res