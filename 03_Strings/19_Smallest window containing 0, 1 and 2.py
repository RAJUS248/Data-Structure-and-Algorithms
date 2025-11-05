def smallest_window(s):

    seen = {'0':-1, '1':-1, '2':-1}

    min_len = float("inf")

    for i in range(len(s)):

        seen[s[i]] = i


        if seen['0'] != -1 and seen['1'] != -1 and seen['2'] != -1:

            window_start = min(seen['0'],seen['1'],seen['2'])

            cur_len = i - window_start + 1

            min_len = min(min_len,cur_len)

    if min_len == float("inf"):

        return -1
    
    else:
        return min_len
    
s = "22001"
    
print(smallest_window(s))