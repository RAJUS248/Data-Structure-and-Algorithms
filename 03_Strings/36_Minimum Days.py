def getMinimumDays(N : int, S : str, P : list[int]) -> int:

    s_lst = list(S)

    conflict = 0

    for i in range(N-1):
        if s_lst[i] == s_lst[i+1]:
            conflict += 1

    if conflict == 0:
        return 0

    for day in range(N):

        i = P[day]

        # left indx
        if i > 0 and s_lst[i] == s_lst[i-1] and s_lst[i] != '?':
            conflict -= 1

        # Right indx

        if i < N-1 and s_lst[i] == s_lst[i+1] and s_lst[i] != '?':
            conflict -= 1

        s_lst[i] = '?'

        if conflict == 0:
            return day + 1
        
    return 0

N = 5
S = "aaabb"
P = [2, 1, 3, 0, 4]
print(getMinimumDays(N,S,P))