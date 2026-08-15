def sec_max(arr):
    maxi = float("-inf") #1
    sec_max = float("-inf") #0
    for num in arr:
        if num > maxi:
            sec_max = maxi
            maxi = num

        elif num > sec_max and num != maxi:
            sec_max = num

    if maxi == float("-inf"):
        print("there is no second largest element list is empty")

    else:
        print(maxi)
        return sec_max
        

arr = [10, 100, 99, 100]

print(sec_max(arr))