def row_with_matrix(arr):
    
    row = len(arr)
    col = len(arr[0])

    max_sum = 0
    max_indx = -1
   

    for i in range(row):

        arr_sum = sum(arr[i])

        if arr_sum > max_sum:
            max_sum = arr_sum
            max_indx = i

         
    return max_indx if max_sum > 0 else -1

        
arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
print(row_with_matrix(arr))



def row_with_matrix_v2(arr):
    
    n = len(arr)
    m = len(arr[0])

    row = 0
    col = m-1

    max_indx = -1

    while row < n and col >= 0:

        if arr[row][col] == 1:
            max_indx = row
            col -= 1

        else:
            row += 1

    return max_indx
    
       
arr = [[0,1,1,1], [0,0,1,1], [0,1,1,1], [0,0,0,0]]
print(row_with_matrix_v2(arr))