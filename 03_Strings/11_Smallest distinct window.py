def findSubString(s):

    count = len(set(s))
    seen = {}
    unique = 0
    l = 0
    mini = float("inf")

    for r in range(len(s)):

        seen[s[r]] = seen.get(s[r], 0) + 1

        if seen[s[r]] == 1:
            unique += 1

        while unique == count:

            mini = min(mini, r-l + 1)

            seen[s[l]] -= 1


            if seen[s[l]] == 0:
                unique -= 1

            l += 1

    return mini if mini != float("inf") else 0

       
s = "aabbbcbbac"
print(findSubString(s))