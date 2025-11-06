def matrix_2D(matrix,target):

    for row in matrix:
        if target in row:
            return True
        
    return False

target = 80
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix_2D(matrix,target))

