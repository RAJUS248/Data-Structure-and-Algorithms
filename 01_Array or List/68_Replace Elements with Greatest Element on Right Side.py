from bisect import insort,bisect_right

def replaceElements(arr):

    maxi = -1

    for i in range(len(arr)-1,-1,-1):

        cur_val = arr[i]
        arr[i] = maxi
        # maxi = max(maxi,cur_val)
        if cur_val > maxi:
            maxi = cur_val

    return arr

arr = [17,18,5,4,6,1]
print(replaceElements(arr))