def Missing_Repeating(arr):

    seen = {}
    repiting = 0

    for num in arr:

        if num not in seen:

            repiting = num

        else: 
            seen[num] = 1

    for i in range(1,len(arr)+1):

        if i not in seen:
            miss = i

    return [repiting,miss]


arr =  [4, 3, 6, 2, 1, 1] 
print(Missing_Repeating(arr))
