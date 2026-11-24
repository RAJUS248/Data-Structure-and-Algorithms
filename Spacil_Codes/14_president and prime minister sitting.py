def sitting(n):
    
    if n == 0 or n == 1:
        return 1
    
    return n * sitting(n-1)

n = 10
print(sitting(n))

def sitting_v2(n):
    
    all_count = 1

    for i in range(1,n):

        all_count *= i

    return 2 * all_count

n = 10
print(sitting_v2(n))


n = 10
fact = [0] * (n + 1)
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i
print(fact[n - 1] * 2)

