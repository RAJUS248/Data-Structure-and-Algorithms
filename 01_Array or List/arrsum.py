def arrsum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum
arr = [1,2,3,4]
print(arrsum(arr))

def arrsum1(arr):
    total = 0
    min1 = arr[0]
    max1 = arr[0]
    for num in arr:
        total += num

        if min1 < num:
            min1 = num

        if max1 > num:
            max1 = num

    min1 = total - min1
    max1 = total - max1
    print( min1,max1)
    
arr = [1,2,3,4]
print(arrsum1(arr))