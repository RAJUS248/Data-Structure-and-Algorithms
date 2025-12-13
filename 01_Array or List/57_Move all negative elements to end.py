def segregateElements(arr):
    pos = []
    neg = []

    for num in arr:
        if num >= 0:
            pos.append(num)

        else:
            neg.append(num)

    res = pos + neg

    for i in range(len(arr)):
        arr[i] = res[i]

    return arr
                   


arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
print(segregateElements(arr))