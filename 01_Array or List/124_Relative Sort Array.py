def relativeSortArray(arr1, arr2):

    count = {}
    for num in arr1:
        count[num] = count.get(num,0)+1

    res = []
    for num in arr2:
        for _ in range(count[num]):
            res.append(num)
            count[num] -= 1

    arr1.sort()
    for num in arr1:
        if count[num] != 0:
            res.append(num)

    return res

    

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1,arr2))


    # res = []
    # for i in range(len(arr2)):
    #     for j in range(len(arr1)):

    #         if arr1[j] == arr2[i]:
    #             res.append(arr1[j])

    # arr1.sort()
    # for num in arr1:
    #     if num not in res:
    #         res.append(num)

    # return res


    