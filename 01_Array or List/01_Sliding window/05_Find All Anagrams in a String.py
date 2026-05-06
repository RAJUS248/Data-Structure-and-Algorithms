def findAnagrams(s, p):

    seen = {}

    for ch in p:
        seen[ch] = seen.get(ch,0) + 1


    window = {}
    res = []

    l = 0

    for r in range(len(s)):

        window[s[r]] = window.get(s[r],0) + 1

        if r - l + 1 > len(p):
            window[s[l]] -= 1

            if window[s[l]] == 0:
                del window[s[l]]
            
            l += 1

        if window == seen:
            res.append(l)

    return res


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))