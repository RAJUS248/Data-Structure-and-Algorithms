def set_bit_count(n):


    count = 0

    while n > 0:

        if n % 2 == 1:
            count += 1

        n //= 2

    return count

def set_bit_count_v2(n2):

    count = 0

    while n2 > 0:

        n2 = n2 & (n2-1)
        count += 1

    return count

n2 = 12
n = 12
print(set_bit_count(n))
print(set_bit_count_v2(n2))

