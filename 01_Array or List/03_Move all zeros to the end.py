def zero_end(arr):
    pos = 0
    for num in arr:
        if num != 0:
            arr[pos] = num
            pos += 1

    for i in range(pos,len(arr)):
        arr[i] = 0
    return arr
        
arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print(zero_end(arr))


# o(n)
def pushZerosAtEnd(arr, n) :
    #Your code goes here

    k = 0

    for i in range(n):

        if arr[i] != 0:
            arr[k],arr[i] = arr[i],arr[k]

            k += 1

    return arr

n = 12
arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print(pushZerosAtEnd(arr,n))



# using extra list
def zero_end_v2(arr):
    new_list = []
    count = 0
    for num in arr:
        if num != 0:
            new_list.append(num)

        if num == 0:
            count += 1

    for _ in range(count):
        new_list.append(0)
    # new_list.extend([0] * count)

    return new_list
      
arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]

print(zero_end_v2(arr))
