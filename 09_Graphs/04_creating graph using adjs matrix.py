def create_undirectional_matrix(edges):

    matrix = [[0]*n for _ in range(n)]  # first put all rows is 0 like [0,0,0,0,0]

    for u,v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1    # undirectional_matrix

    return matrix
n = 5
edges = [[0,1], [0,2], [1,2], [3,4]]
undirectional_matrix = create_undirectional_matrix(edges)

print("undirectional_matrix")
for row in undirectional_matrix:
    print(row)



# directional_matrix

def create_directional_matrix(edges):

    matrix = [[0]*n for _ in range(n)]  # first put all rows is 0 like [0,0,0,0,0]

    for u,v in edges:
        matrix[u][v] = 1
    

    return matrix
n = 5
edges = [[0,1], [0,2], [1,2], [3,4]]
directional_matrix = create_directional_matrix(edges)

print("\ndirectional_matrix")
for row in directional_matrix:
    print(row)

# res = []

# for _ in range(4):
#     res.append([0]*4)

# print("\n res \n",res)