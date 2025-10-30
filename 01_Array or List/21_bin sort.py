def binSort(arr):
        # code here
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
            
        return arr

arr = [1,0,1,0,0,0]
print(binSort(arr))


def binSort_v2(arr):
        # code here
        
        lst1 = []
        lst2 = []

        for num in arr:
            if num == 0: 
                lst1.append(num)

            else:
                lst2.append(num)

        return lst1 + lst2
                
                    

arr = [1,0,1,0,0,0]
print(binSort_v2(arr))


def binSort_v3(arr):
    arr.sort()
    return arr
arr = [1,0,1,0,0,0]
print(binSort_v3(arr))


def binSort_v4(arr):
    
    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] == 0:
            start += 1

        elif arr[end] == 1:
             end -= 1

        else:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1

    return arr


arr = [0,0,1,1,0,1,0,1,1,0]
print(binSort_v4(arr))