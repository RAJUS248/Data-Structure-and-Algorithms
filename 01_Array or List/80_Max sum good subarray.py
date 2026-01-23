from collections import defaultdict
def Max_sum_good_subarray(N,K,A):

    if K >= len(set(A)):
        max_sum = 0
        current_sum = 0
        for x in A:
            current_sum = max(x, current_sum + x)
            max_sum = max(max_sum, current_sum)
        return max_sum

    l = 0
    cur_sum = 0
    max_sum = 0
    freq = defaultdict(int)

    for r in range(N):

        cur_sum += A[r]
        freq[A[r]] += 1

        while len(freq) > K:

            cur_sum -= A[l]
            freq[A[l]] -= 1

            if freq[A[l]] == 0:
                del(freq[A[l]])

            l += 1

        max_sum = max(cur_sum,max_sum)

    return max_sum


N = 5
K = 3
A = [-1,1,3,2,-1]
print(Max_sum_good_subarray(N,K,A))