n = int(input())
arr = list(map(int, input().split()))  # convert to list so we can index

max1 = float('-inf')  # largest
max2 = float('-inf')  # second largest

for num in arr:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num
    
if max2 == float('-inf'):
    print("No second largest number")
else:
    print(max2)
