def Rearrange_an_array(arr):

    arr2 = []

    for i in range(len(arr)):

        arr2.append(arr[arr[i]])

    return arr2

arr = [4, 0, 2, 1, 3]
print(Rearrange_an_array(arr))


#or

def Rearrange_an_array_v2(arr):

    n = len(arr)

    for i in range(n):

        new_val = arr[arr[i]] % n 

        arr[i] = arr[i] + (n * new_val)

    for j in range(n):
        arr[j] //= n

    return arr
arr = [4, 0, 2, 1, 3]
print(Rearrange_an_array_v2(arr))