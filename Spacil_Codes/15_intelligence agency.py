def intelligence_agency(N,R):

    if R == 0:
        return 0
    
    N_sum = 0
    while N > 0:

        last_digit = N % 10
        N_sum += last_digit
        N //= 10

    N_sums_sum = N_sum * R
    
    while N_sums_sum >= 10:
        ans = 0
        temp = N_sums_sum
        while temp > 0:

            last_digit = temp % 10
            ans += last_digit
            temp //= 10

        N_sums_sum = ans

    return N_sums_sum

N = 199
R = 1
print(intelligence_agency(N,R))