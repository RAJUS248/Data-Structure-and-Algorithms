def minPathSum(grid):

    rows = len(grid)
    cols = len(grid[0])

    if rows == 0:
        return 0

    # Fill first row
    for c in range(1,cols):   
        grid[0][c] += grid[0][c-1]

    # Fill first column
    for r in range(1,rows):
        grid[r][0] += grid[r-1][0]

    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[rows-1][cols-1],grid          

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))


