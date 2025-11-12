def Min_Subsets(arr):

    arr.sort()

    count = 1
    for i in range (len(arr)-1):

        if arr[i]+1 != arr[i+1]:
            count += 1

    return count

arr = [100, 56, 5, 6, 102, 58, 101, 57, 7, 103] 
print(Min_Subsets(arr))