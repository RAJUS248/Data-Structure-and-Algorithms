def rearrange_array_increas_decreas_order(arr):

    arr.sort()       # sort the given arr
        
    full_len = len(arr) - 1
    half_len = len(arr)//2        # find mid

    while half_len < full_len:

        # swap right half
        arr[half_len],arr[full_len] = arr[full_len],arr[half_len]  

        half_len += 1   # increase 1 step 
        full_len -= 1   # decrease 1 step

    return arr

arr = [8,7,1,6,5,9]
arr2 = [4,2,8,6,15,5,9,20]
print(rearrange_array_increas_decreas_order(arr))
print(rearrange_array_increas_decreas_order(arr2))