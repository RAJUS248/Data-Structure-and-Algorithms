def sec_lowest(arr):
    mini = float("inf")
    secmini = float("inf")

    for num in arr:
        if num < mini:
            secmini = mini
            mini = num

        elif num < secmini and num != mini:
            secmini = num

    if secmini == float('inf'):
        print("No second minimum (all elements equal or single element).")
    else:
        print(secmini)

arr = [0,0,1]
sec_lowest(arr)