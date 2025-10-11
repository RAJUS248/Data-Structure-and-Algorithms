def sec_max(arr):
    maxi = float("-inf")
    sec_max = float("-inf")
    for num in arr:
        if num > maxi:
            sec_max = maxi
            maxi = num

        elif num > sec_max and num != maxi:
            sec_max = num

    if maxi == float("-inf"):
        print("there is no second largest element list is empty")

    else:
        return sec_max

arr = [10, 20, 4, 45, 99]

print(sec_max(arr))