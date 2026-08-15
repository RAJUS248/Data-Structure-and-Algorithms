def sum_digits(num):

    while num > 9:

        s = 0
        while num > 0:
            s += num % 10
            num //= 10

        num = s

    return num

num = 987
print(sum_digits(num))


n = 987

while n > 9:
    sums = 0
    for d in str(n):
        sums += int(d)
    n = sums
print(n)