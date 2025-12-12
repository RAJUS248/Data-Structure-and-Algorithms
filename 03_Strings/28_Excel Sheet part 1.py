def ExcelColumn(N):

    s = ''

    while N > 0:

        N -= 1
        s += chr((N % 26) + 65)
        N //= 26
        

    return s[::-1]

N = 51
print(ExcelColumn(N))