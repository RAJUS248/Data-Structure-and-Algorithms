def most_water(arr):

    maxi = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):

            distance = j-i
            hight = min(arr[i],arr[j])

            area = hight * distance

            if area > maxi:
                maxi = area

    return maxi

arr = [1, 5, 4, 3]
print(most_water(arr))


def most_water_v2(arr):

    maxi = 0
    i = 0
    j = len(arr)-1

    while i < j:

        distance = j-i
        hight = min(arr[i],arr[j])

        area = hight * distance

        if area > maxi:
            maxi = area

        if arr[i] < arr[j]:
            i += 1
        
        else:
            j -= 1
       

    return maxi

arr = [1, 5, 4, 3]
print(most_water_v2(arr))