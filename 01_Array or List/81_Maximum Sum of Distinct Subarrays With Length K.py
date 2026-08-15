from collections import defaultdict
def maximumSubarraySum(nums, k):
    l = 0
    cur_sum = 0
    max_sum = 0
    freq = defaultdict(int)

    for r in range(len(nums)):

        cur_sum += nums[r]
        freq[nums[r]] += 1

        if r - l + 1 > k:

            freq[nums[l]] -= 1
            cur_sum -= nums[l]

            if freq[nums[l]] == 0:
                del(freq[nums[l]])

            l += 1

        if r - l + 1 == k and len(freq) == k:
            max_sum = max(max_sum,cur_sum)

    return max_sum

nums = [1,5,4,2,9,9,9]
k = 3
print(maximumSubarraySum(nums,k))