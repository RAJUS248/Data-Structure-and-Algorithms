def sum_of_even_odd(num):

    even = 0
    odd = 0
    
    while num > 0:

        ld = num % 10

        if ld % 2 == 0:
            even += ld

        else:
            odd += ld

        num = num // 10

    return even, odd

num = 132456
print(sum_of_even_odd(num))