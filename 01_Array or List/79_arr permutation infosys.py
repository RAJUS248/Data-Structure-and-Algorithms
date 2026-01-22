from itertools import permutations
def array_permutation(N,K,arr):
    perm = set(permutations(arr))

    count = 0
    for p in perm:

        assets = 0
        for i in range(len(p)-1):
            if p[i] < p[i+1]:
                assets += 1

        if assets == K:
            count += 1

    return count

N = 3
K = 1
arr = [3,2,1]
print(array_permutation(N,K,arr))
