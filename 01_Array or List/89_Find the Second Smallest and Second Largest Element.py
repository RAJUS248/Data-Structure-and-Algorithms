def find_sec_smallest_and_largest(arr):

    smallest = float('inf')
    sec_smallest = float('inf')
    
    largest = float('-inf')
    sec_largest = float('-inf')

    for num in arr:

        if num < smallest:
            sec_smallest = smallest
            smallest = num

        elif sec_smallest > num and num != smallest:
            sec_smallest = num 

        if num > sec_largest:
            sec_largest = largest
            largest = num

        elif sec_largest > num and num != largest:
            sec_largest = num

    return sec_largest,sec_smallest
            
arr = [1, 2, 4, 7, 7, 5]
print(find_sec_smallest_and_largest(arr))