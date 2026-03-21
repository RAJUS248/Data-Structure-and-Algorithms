def findSubString(str):

    start = 0
    seen = set(str)
    for i in range(1,len(str)):

        if str[start] == str[i]:
            start += 1

        if str[i] in seen:
            seen.remove(str[i])

        else:
            seen.add(str[i])
            start += 1

    return seen

str = "aabcbcdbca"
print(findSubString(str))