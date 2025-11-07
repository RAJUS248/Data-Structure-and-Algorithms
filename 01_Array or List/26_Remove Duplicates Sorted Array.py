def remove_dublicate(arr):
    
    arr2 = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr2.append(arr[i])

    return arr2

arr = [1, 2,4,4]
print(remove_dublicate(arr))


def remove_dublicate_v2(arr):

    seen = set()
    arr2 = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            arr2.append(num)

        
    return arr2
arr = [1, 2,2,4,4]
print(remove_dublicate_v2(arr))