def Armstrong_number(num):
    
    n = len(str(num))
    res = 0

    temp = num 

    for _ in range(n):

        last_digit = temp % 10

        res += last_digit**n
    
        temp = temp//10

    if res == num:
        print("true")

    else:
        print("false")

num = 351
Armstrong_number(num)
