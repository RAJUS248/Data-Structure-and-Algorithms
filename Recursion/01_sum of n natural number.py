def sum_of_n_natural_number(n):

    if n < 1:
        return 0
    
    return n + sum_of_n_natural_number(n-1)

# n = int(input('enter natural number: '))
# print(sum_of_n_natural_number(n))


def sum_of_n_even_number(n):

    if n <= 0:
        return 0
    
    return n * 2 + sum_of_n_natural_number((n-1)*2)

n = int(input('enter even number: '))
print(sum_of_n_even_number(n))