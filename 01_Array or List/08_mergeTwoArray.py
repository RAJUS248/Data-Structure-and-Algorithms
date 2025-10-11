def merge2array(arr1,arr2):

    list = []
    for i in arr1+arr2:
        list.append(i)

    list.sort()
    print(list)

arr1 = [1,3,4,5]
arr2 = [2,6,8,9]
merge2array(arr1,arr2)

def in_place(arr,arr2):
    i = 0
    

    while i < len(arr1):
        if arr1[i] > arr2[0]:
            arr1[i],arr2[0] = arr2[0],arr1[i]
            arr2.sort()
        i += 1

    return arr1 + arr2
   
arr1 = [1,5,3,4]
arr2 = [1,3,2,6,10,11]

print(in_place(arr1,arr2))

def merge_two_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)

    i = 0
    j = 0

    while i < m and j < n:
        if arr1[i] > arr2[j]:
            # swap
            arr1[i], arr2[j] = arr2[j], arr1[i]
             # keep arr2 sorted
        i += 1
    array = arr1 + arr2
    array.sort()
    return array

arr1 = [1,5,3,4]
arr2 = [10,3,2,11,6,1]

print(merge_two_arrays(arr1, arr2))
