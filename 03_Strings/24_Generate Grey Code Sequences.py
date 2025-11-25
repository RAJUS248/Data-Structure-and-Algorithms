def graycode(n):

    res = []
    for i in range(0, (2**n)):

        code = i ^ (i >> 1)

        bin_str = f"{code :0{n}b}"
        res.append(bin_str)
        # res.append(bin(code)[2:])

    return res

n = 2
print(graycode(n))
