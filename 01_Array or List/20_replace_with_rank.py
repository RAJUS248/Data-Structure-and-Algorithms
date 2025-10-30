def ranking(arr):
    
    sort_list = sorted(set(arr))

    seen = {}

    #for i in range(len(sort_list)):
        #seen[sort_list[i]] = i + 1

    for i,val in enumerate(sort_list):
        seen[val] = i+1

    print(seen)

    res = []

    for num in arr:
        res.append(seen[num])

    print(res)

arr = [20,15,26,2,98,6]
ranking(arr)



#Example 1 :
#Input : 20 15 26 2 98 6
#Output : 4 3 5 1 6 2
"""
arr = [1, 5, 8, 15, 8, 25, 9]

arr1 = sorted(set(arr))
print("sorted",arr1)
print("unsorted",arr)


for i in range(len(arr)):
    for j in range(len(arr1)):
        if arr[i] == arr1[j]:
            print(j+1,end=  "   ")

"""
