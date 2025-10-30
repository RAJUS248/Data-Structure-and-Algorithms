def Rotate_Array_by_One(arr):
    
    copy = arr.copy()
    arr2 = []
    num = arr.pop()
    arr2.append(num)

    for i in range(len(arr)):

        arr2.append(arr[i])

    print(copy)
    return arr2
    

arr = [1, 2, 3, 4, 5]
print(Rotate_Array_by_One(arr))


def rotate_by_one_slice(arr):
    return [arr[-1]] + arr[:-1]

arr = [1, 2, 3, 4, 5]
print(rotate_by_one_slice(arr))


def rotate_in_place(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    last = arr[-1]
    
    # shift all elements right by one
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = last
    return arr


# Example tests
print(rotate_in_place([1, 2, 3, 4, 5])) 


from collections import deque

def rotates(arr):
    dq = deque(arr)

    dq.rotate(1)

    print(list(dq))
arr = [1, 2, 3, 4, 5]
rotates(arr)