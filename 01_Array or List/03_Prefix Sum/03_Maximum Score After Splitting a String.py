def maxScore(s):

    lst = []
    for ch in s:
        lst.append(int(ch))

    left_zero_count = 0
    right_sum = sum(lst)
    max_score = 0

    for i in range(len(lst)-1):

        right_sum -= lst[i]
        if lst[i] == 0:
            left_zero_count += 1

        max_score = max(max_score,left_zero_count + right_sum)  

    return max_score

def max_Score_v2(s):

    left_zero_count = 0
    right_sum = s.count('1')
    max_score = 0

    for ch in range(len(s)-1):

        
        if ch == '0':
            left_zero_count += 1

        else:
            right_sum -= 1

        max_score = max(max_score,left_zero_count + right_sum)  

    return max_score
s = "1111"
print(maxScore(s))
print(max_Score_v2(s))