def Matrix_Trapezoid(n):

    matrix = []
    for i in range(1,n+1):
        lst = []
        for j in range(i,n+i):

            lst.append(j)

        matrix.append(lst)

    return matrix

n = 3
# print(Matrix_Trapezoid(n))


def solve_matrix_trapezoid():

    matrix = []

    for _ in range(3):

        row = list(map(int,input().split()))

        matrix.append(row)

    print(matrix)

    counts = []

    for row in matrix:

        # counting non-zeros
        count = 0
        for num in row:

            if num != 0:
                count += 1

        counts.append(count)
    
    trapezoid_count = (counts[0] > counts[1]) and (counts[1] > counts[2])

    if trapezoid_count:

        return sum(matrix[0])
    
    else:

        product = 1
        for num in matrix[0]:

            product *= num

        return product


res = solve_matrix_trapezoid()
print(res)