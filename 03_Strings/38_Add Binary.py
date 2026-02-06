def addBinary(a, b):
    
    i = len(a)-1
    j = len(b)-1

    carry = 0
    res = ''

    while i >= 0 or j >= 0 or carry:

        if i >= 0:
            a_val = int(a[i])
        
        else:
            a_val = 0

        if j >= 0:
            b_val = int(b[j])

        else:
            b_val = 0

        total = a_val + b_val + carry

        res += str(total%2)
        carry = total // 2

        i -= 1
        j -= 1

    return res[::-1]


a ='11'
b = '1'
print(addBinary(a,b))