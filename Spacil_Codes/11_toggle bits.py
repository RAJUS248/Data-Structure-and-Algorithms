def toggle(n):

    # bits = n.bit_length()

    temp = n
    bits = 0
    
    while temp > 0:
        bits += 1
        temp = temp >> 1 # temp //= 2


    mask = (1 << bits) - 1

    return n ^ mask

n = 10
print(toggle(n))

