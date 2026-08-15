def findMaxAverage(nums, k):

    l = 0
    k_sum = 0
    max_k_avrage = float('-inf')
    for r in range(len(nums)):

        if (r - l) < k:
            k_sum += nums[r]

        elif r-l+1 == k:
            max_k_avrage = max(max_k_avrage, k_sum)

        else:
            max_k_avrage = max(max_k_avrage, k_sum)
            k_sum += nums[r]
            k_sum -= nums[l]
            max_k_avrage = max(max_k_avrage, k_sum)
            l += 1
            
    if r-l+1 == k:
            max_k_avrage = max(max_k_avrage, k_sum)

    return max_k_avrage/float(k)

nums = [4,0,4,3,3]#[-5,-4,-3] #[1,12,-5,-6,50,3]
k = 5
print(findMaxAverage(nums,k))


# window_sum = sum(nums[:k])
#         max_sum = window_sum

#         for i in range(k,len(nums)):

#             window_sum -= nums[i-k]  # remove left element
#             window_sum += nums[i]  # add new right element

#             max_sum = max(max_sum,window_sum)

#         return max_sum / float(k)