def isHappy(n):

    temp = n
    n_sum = 0
    seen = set()
    seen.add(n)
    while temp:

        ld = temp % 10
        n_sum += ld*ld
        temp //= 10

        if temp == 0:
            if n_sum == 1:
                return True
            
            if n_sum in seen:
                return False
            
            seen.add(n_sum)

            temp = n_sum
            n_sum = 0

            

n = 19
print(isHappy(n))


def isHappy_v2(n):

    temp = n
    seen = set()

    while temp != 1:

        if temp in seen:
            return False
        seen.add(temp)

        
        n_sum = 0
        while temp:

            ld = temp % 10
            n_sum += ld*ld
            temp //= 10

        temp = n_sum

    return True
            

n = 19
print(isHappy_v2(n))