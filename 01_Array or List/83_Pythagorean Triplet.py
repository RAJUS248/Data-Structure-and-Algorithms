def pythagoreanTriplet(arr):

    seen = set()

    for num in arr:
        seen.add(num*num)

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):

            if arr[i]**2 + arr[j]**2 in seen:
                return True
        
    return False

arr = [3, 2, 4, 6, 5]
print(pythagoreanTriplet(arr))