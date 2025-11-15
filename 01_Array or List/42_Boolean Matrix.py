def bool_matrix(mat):

    row = len(mat)
    col = len(mat[0])

    row_mark = [0] * row
    col_mark = [0] * col

    for r in range(row):
        for c in range(col):

            if mat[r][c] == 1:
                row_mark[r] = 1
                col_mark[c] = 1

    for r in range(row):
        for c in range(col):

            if row_mark[r] == 1 or col_mark[c] == 1:
                mat[r][c] = 1                

    return mat



mat = [
  [0, 1, 0],
  [0, 0, 0],
  [1, 0, 0]
]

print(bool_matrix(mat))

