def sort_alph(s):

    upper = []
    lower = []
    res = ""
    for ch in s:
        if "A" <= ch <= "Z":
            upper.append(ch)

        else:
            lower.append(ch)
            

    upper.sort()
    lower.sort()

    i = j = 0

    for ch in s:
        if ch.isupper():
            res += upper[i]
            i += 1

        else:
            res += lower[j]
            j += 1

    return res

s = "GEekS"
print(sort_alph(s))