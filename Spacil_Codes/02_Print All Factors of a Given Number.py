def print_factor(num):

    res = []

    for i in range(1,num+1):

        if num % i == 0:
            res.append(i)

    return res

num = 20
print(print_factor(num))


def print_factor_v2(num):

    res = []

    for i in range(1,num//2 + 1):

        if num % i == 0:
            res.append(i)

    res.append(num)

    return res

num = 20
print(print_factor_v2(num))



from math import sqrt
def print_factor_v3(num):

    res = []

    for i in range(1,int(sqrt(num))+1):

        if num % i == 0:
            res.append(i)

            if num//i != i:
                res.append(num//i)
    
    res.sort()
    return res

num = 20
print(print_factor_v3(num))