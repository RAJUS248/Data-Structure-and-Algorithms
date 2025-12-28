from bisect import bisect_right,insort
def findLeastGreater(arr):
    n = len(arr)
    res = [-1] * n
    sort_lst = []

    for i in range(n-1,-1,-1):

        idx = bisect_right(sort_lst,arr[i])

        if idx < len(sort_lst):
            res[i] = sort_lst[idx]
        
        else:
            res[i] = -1

        insort(sort_lst,arr[i])

    return res

    
arr = [4, 8, 2, 7, 5, 9, 3]
print(findLeastGreater(arr))