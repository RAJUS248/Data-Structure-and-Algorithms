def numOfSubarrays(arr, k, threshold):

    l = 0
    cur_sum = 0
    count = 0
    for r in range(len(arr)):

        cur_sum += arr[r]

        if r - l + 1 == k:
            
            if cur_sum//k >= threshold:
                count += 1

            cur_sum -= arr[l]
            l += 1


    return count
              
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(numOfSubarrays(arr,k,threshold))