def rob_house(arr):
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    for first in range(0,len(arr),2):
        arr1.append(arr[first])

    for sec in range(1,len(arr),2):
        arr2.append(arr[sec])

    for thrd in range(0,len(arr),3):
        arr3.append(arr[thrd])

    for forth in range(1,len(arr),3):
        arr4.append(arr[forth])

    a = sum(arr1)
    b = sum(arr2)
    c = sum(arr3)
    d = sum(arr4)
    print(max(a,b,c,d))



arr = [6, 7, 1, 30, 8, 2, 4]
rob_house(arr)

def rob_house_v2(arr):
    prev1 = 0
    prev2 = 0

    for num in arr:
        temp = prev1
        prev1 = max(prev2 + num ,prev1)
        prev2 = temp

    return prev1

arr = [6, 7, 1, 30, 8, 2, 4]
print(rob_house_v2(arr))