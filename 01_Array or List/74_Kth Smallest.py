import heapq
def Kth_Smallest(arr,k):
    max_elements = []

    for num in arr:
        heapq.heappush(max_elements,-num)

        if len(max_elements) > k:
            heapq.heappop(max_elements)

    return -max_elements[0]


arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

print(Kth_Smallest(arr,k))




def Kth_Smallest_v2(arr,k):

    heapq.heapify(arr)

    for _ in range(k-1):
        heapq.heappop(arr)

    return heapq.heappop(arr)

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

print(Kth_Smallest_v2(arr,k))