def majorityElement(arr):

    n = len(arr)
    seen = {}

    for num in arr:

        seen[num] = seen.get(num,0) + 1

    for num in arr:
        if seen[num] > n//2:
            return num
        
    return -1

arr = [3,3,4,2,3]
print(majorityElement(arr))


def majorityElement_v2(arr):

    n = len(arr)
    
    can = None
    count = 0

    for num in arr:

        if count == 0:

            can = num
            count = 1

        elif num == can:

            count += 1

        else:
            count -= 1

    if arr.count(can) > n // 2:

        return can
    
    return -1

arr = [3,3,4,2,3]
print(majorityElement_v2(arr))