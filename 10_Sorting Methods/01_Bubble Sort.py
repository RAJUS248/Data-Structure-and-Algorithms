def Bubble_sort(arr):

    size = len(arr)

    for read in range(size):
        swap = False

        for index in range(0,size-read-1):

            if arr[index] > arr[index+1]:
                
                temp = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = temp

                swap = True
                
        if swap != True:
            break

    return arr

arr = [1,9,2,4,9,3,0,100,54,76,2,5,4,100]
print(Bubble_sort(arr))