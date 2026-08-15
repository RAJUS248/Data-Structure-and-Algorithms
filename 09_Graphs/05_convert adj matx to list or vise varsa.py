from collections import defaultdict
def matrix_to_list(matrix_graph):

    n  = len(matrix_graph)
    list_graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if matrix_graph[i][j] == 1:
                list_graph[i].append(j)

    return dict(list_graph)

matrix_graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0]
]

print("matrix_to_list\n",matrix_to_list(matrix_graph))


def list_to_matrix(list_graph):

    n = len(list_graph)

    matrix = [[0]*n for _ in range(n)]

    for u in list_graph:
        for v in list_graph[u]:
            matrix[u][v] = 1

    return matrix

list_graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}
matrix_print = list_to_matrix(list_graph)

print("\nlist_to_matrix")
for row in matrix_print:
    print(row)