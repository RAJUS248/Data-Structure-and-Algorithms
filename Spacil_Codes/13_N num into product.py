def n_num_into_product(n):

    if n == 0:
        return 0
    
    temp = n
    product = 1
    while temp > 0:

        last_dig = temp % 10
        product *= last_dig
        temp = temp // 10

    return product

n = 0
print(n_num_into_product(n))