def convertToTitle(columnNumber):

    s = ''

    while columnNumber > 0:
        columnNumber -= 1
        s += chr((columnNumber % 26) + 65)   # 65 = ord('A')
        columnNumber //= 26

    return s[::-1]

columnNumber = 7975903933

print(convertToTitle(columnNumber))

