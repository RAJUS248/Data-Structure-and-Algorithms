import heapq
def findKthLargest(nums, k):

    max_element = []

    for num in nums:
        heapq.heappush(max_element,num)

        if len(max_element) > k:
            heapq.heappop(max_element)

    return max_element[0]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))



def findKthLargest_v2(nums, k):
    nums.sort()
    return nums[-k]
    

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest_v2(nums,k))