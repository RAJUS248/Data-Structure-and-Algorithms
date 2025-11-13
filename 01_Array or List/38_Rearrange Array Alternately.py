def rearrange(arr):

    n =len(arr)
    arr2 = []
    low = 0
    high = n-1

    while low <= high:

        arr2.append(arr[high])
        high -= 1

        arr2.append(arr[low])
        low += 1 

    for i in range(n):
        arr[i] = arr2[i]

    return arr

arr = [1, 2, 3, 4, 5, 6]
print(rearrange(arr))


# or

def rearrange_v2(arr):

    n = len(arr)

    min_indx = 0

    max_indx = n-1

    max_val = arr[n - 1] + 1

    for i in range(n):

        if i % 2 == 0:

            new_val = (arr[max_indx] % max_val)

            arr[i] = arr[i] + (new_val * max_val)

            max_indx -= 1

        else:

            new_val = (arr[min_indx] % max_val)

            arr[i] = arr[i] + (new_val * max_val)

            min_indx += 1

        
    for i in range(n):
        arr[i] = arr[i] // max_val

    return arr

        


arr = [1, 2, 3, 4, 5, 6]
print(rearrange_v2(arr))