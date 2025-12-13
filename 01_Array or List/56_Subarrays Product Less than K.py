def countSubArrayProductLessThanK_v2(arr, k):

    if k <= 1:
        return 0

    count = 0
    l = 0
    prod = 1

    for r in range(len(arr)):

        prod *= arr[r]

        while prod >= k and l <= r:
            prod //= arr[l]
            l += 1

        count += (r - l + 1)


    return count

arr = [1, 2, 3, 4]
k = 10
print(countSubArrayProductLessThanK_v2(arr,k))