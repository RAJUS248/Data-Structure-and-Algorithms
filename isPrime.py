
def is_prime(num):
    if num <= 1:
        return "Not prime"
    
    if num == 2:
        return "prime"
    
    if num % 2 == 0:
        return "not prime"
    
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return "not prime"
        
    return "prime"

print(is_prime(7))
        


def is_prime_v2(num):
    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
        
    return True

num = 3
for j in range(2, num + 1):
    if is_prime_v2(j):
        print(j, end = " ")

print(is_prime_v2(num))
        