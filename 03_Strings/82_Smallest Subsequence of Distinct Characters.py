def smallestSubsequence(s):
        
        seen = [0] * 26

        for i in range(len(s)):
            seen[ord(s[i])-ord("a")] = i

        sen = set(s[0])
        res = [s[0]]

        for i in range(1,len(s)):

            if s[i] < res[len(res)-1]:
                prev = res[len(res)-1]

                while i-1 < seen[ord(prev) - ord("a")]:
                    rm = res.pop()
                    sen.remove(rm)


                    if res:
                        prev = res[len(res)-1]

                    else:
                        break

                if s[i] not in sen:
                    res.append(s[i])
                    sen.add(s[i])

            elif s[i] not in sen:
                res.append(s[i])
                sen.add(s[i])
                

        return "".join(res)
s = "cbabc"
print(smallestSubsequence(s))