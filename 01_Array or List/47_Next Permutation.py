def next_permutation(arr):

    n = len(arr)
    i = n-2

    while i >= 0 and arr[i] >= arr[i+1]:

        i -= 1

    if i >= 0:
        j = n -1

        while arr[j] <= arr[i]:
            j -= 1

        arr[i],arr[j] = arr[j],arr[i]

    left, right = i + 1, n - 1
    while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

arr = [1,3,2,5,4]
print(next_permutation(arr))