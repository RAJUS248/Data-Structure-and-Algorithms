def topKFrequent(nums, k):
        
        freq = {}

        for num in nums:

            freq[num] = freq.get(num,0) + 1

        freq_sort = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        
        res = []
        for num,frq in freq_sort:

            if len(res) < k:
                res.append(num)

            else:
                break

        return res

nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums,k))