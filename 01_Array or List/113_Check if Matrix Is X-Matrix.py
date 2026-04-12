def checkXMatrix(grid):

    rows = len(grid)
    cols = len(grid[0])
    n = len(grid)
    for r in range(rows):
        for c in range(cols):

            if r == c or r + c == n-1:

                if grid[r][c] == 0:
                    return False
                
            else:
                if grid[r][c] != 0:
                    return False
                
    return True

    

grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
print(checkXMatrix(grid))


# for r,c in zip(range(rows),range(cols)):
    #     if grid[r][c] == 0:
    #         return False
    
    # for r,c in zip(range(rows),range(cols-1,-1,-1)):
    #     if grid[r][c] == 0:
    #         return False
    
    # for r in range(1,rows-1):
    #     if grid[r][0] != 0:
    #         return False
        
    #     if grid[r][rows-1] != 0:
    #         return False

    # for c in range(1,cols-1):

    #     if grid[0][c] != 0:
    #         return False
        
    #     if grid[cols-1][c] != 0:
    #         return False
        
    # return True