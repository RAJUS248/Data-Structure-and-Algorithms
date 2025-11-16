def max_Triplet(arr):

    max1 = max2 = max3 = float("-inf")
    min1 = min2  = float("inf")

    for num in arr:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num

        elif num > max2:                # and num != max1:
            max3 = max2
            max2 = num

        elif num > max3:                 #  and num != max2 and num != max1:
            max3 = num

        if num < min1:
            min2 = min1
            min1 = num

        elif num < min2:      # and num != min1:
            min2 = num



    return max((max1 * max2 * max3), (min1 * min2 * max1))


arr = [-3, -5, 1, 0, 8, 3, -2]
print(max_Triplet(arr))