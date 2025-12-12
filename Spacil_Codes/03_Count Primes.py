def Count_Primes(n:int) -> int:

    if n <= 1:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    i = 2

    while i * i < n:

        if is_prime[i]:
            for j in range(i*i,n,i):
                is_prime[j] = False

        i += 1
    return sum(is_prime)

n = 11
print(Count_Primes(n))


def Count_Primes_v2(n:int) -> int:

    if n <= 1:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(3,int(n**0.5)+1,2):
        
        if is_prime[i]:

            for j in range(i*i,n):
                is_prime[j] = False

    
    count = 1
    for k in range(3,n,2):

        if is_prime[k] == True:
            count += 1

    return count
    

n = 11
print(Count_Primes_v2(n))