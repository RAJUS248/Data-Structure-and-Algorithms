def neutralize_capsules(N,A):

    # A  = A[:]
    
    i = 0

    while i < N - 1:

        if A[i] == 0:
            i += 1
            continue

        s = 0

        for j in range(i,N-1):

            if A[j] == 0:
                break
            s += A[j]

            if s == A[j+1]:
                for k in range(i, j+2):
                    A[k] = 0

                i = j+2
                break

        else:
            i += 1
    
    return A

N = 6
A = [2, 2, 4, 5, 5, 10]
print(neutralize_capsules(N,A))

