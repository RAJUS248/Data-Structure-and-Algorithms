def titleToNumber(columnTitle):

    res = 0
    for ch in columnTitle:

        val = ord(ch) - ord('A') + 1

        res = (res * 26) + val

    return res

columnTitle = 'YUGQDKW'
print(titleToNumber(columnTitle))