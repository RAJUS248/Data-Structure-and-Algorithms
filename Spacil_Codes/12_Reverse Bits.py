def reverseBits(n):
    
    res = 0
    for _ in range(4):

        bit = n & 1
        res <<= 1
        res |= bit
        n >>= 1

    return res

n = 12
print(reverseBits(n))