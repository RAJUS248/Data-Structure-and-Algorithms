def longest_substr(string):
    sets = set()
    left = 0
    res = 0

    for right in range(len(string)):
        while string[right] in sets:
            sets.remove(string[left])
            left += 1

        sets.add(string[right])

        res = max(res,right-left + 1)

    return res

string = "abcdecdcb"
print(longest_substr(string))