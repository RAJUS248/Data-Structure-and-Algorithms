def removeAllOccurrencesOfChar(s, ch):

    if not s:
        return s

    res = ''
    for let in s:

        if let != ch:
            res += let

    return res

s = 'aabccbaa'
ch = 'a'
print(removeAllOccurrencesOfChar(s,ch))