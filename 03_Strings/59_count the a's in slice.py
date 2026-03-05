def count_num_of_a(s,L):

    max_a = 0

    for i in range(0,len(s),L):

        cur_count = 0   # print(s[i:i+L])

        for ch in s[i:i+L]:
            if ch == 'a':
                cur_count += 1

        max_a = max(max_a,cur_count)

    return max_a

s = "bbbaaababa"
L = 3
print(count_num_of_a(s,L))


def count_num_of_a_v2(s,L):

    max_a = 0
    cur_count = 0

    for i in range(len(s)):

        if i % L == 0:
            max_a = max(max_a,cur_count)
            cur_count = 0

        if s[i] == 'a':
            cur_count += 1

    return max_a

s = "bbbaaababa"
L = 3
print(count_num_of_a_v2(s,L))