def transpose(matrix):
        
        res = []

        for i in range(len(matrix[0])):
            mat = []
            for j in range(len(matrix)):

                mat.append(matrix[j][i])
            
            res.append(mat)

        return res
        
matrix = [[1,2,3],[4,5,6]]
print(transpose(matrix))