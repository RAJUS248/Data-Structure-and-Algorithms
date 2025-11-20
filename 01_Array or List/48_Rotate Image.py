def Rotate_Image(matrix):

    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
    for i in range(n):
        # matrix[i].reverse()
        left = 0
        right = n-1

        while left < right:
            matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
            left += 1
            right -= 1



    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Rotate_Image(matrix))