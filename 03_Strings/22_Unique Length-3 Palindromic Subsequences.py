from collections import Counter
def countPalindromicSubsequence(s):

    res = set()
    left = set()
    right = Counter(s)

    for m in s:
        right[m] -= 1
        for c in left:
            if right[c] > 0:
                res.add((m,c))
        
        left.add(m)
    
    return len(res)

s = "aabca"
print(countPalindromicSubsequence(s))




def countPalindromicSubsequence_v2(s):

    n = len(s)
    res = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] == s[k]:
                    res.add((s[i],s[j],s[k]))

    return len(res)

s = "aabca"
print(countPalindromicSubsequence_v2(s))


def countPalindromicSubsequence_v3(s):

    seen = set(s)
    count = 0

    for ch in seen:

        first = s.find(ch)
        last = s.rfind(ch)

        if first < last:

            mid_ch = set(s[first+1 : last])

            count += len(mid_ch)

    return count

s = "aabcaded"
print(countPalindromicSubsequence_v3(s))
