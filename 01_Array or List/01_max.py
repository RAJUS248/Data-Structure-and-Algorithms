def sec_max(arr):
    maxi = float("-inf")
    for num in arr:
        if num > maxi:
            maxi = num
    return maxi

arr = [10, 20, 4, 45, 99]

print(max(arr))