def squre_sum_of_prime_numbers(arr):

    def is_prime(num):

        if num < 2:
            return False
        
        for i in range(2,int(num ** 0.5)+1):

            if num % i == 0:
                return False
            
        return True

    squre_sum = 0
    for num in arr:

        if is_prime(num):
            squre_sum += num ** 2

    return squre_sum

n = int(input('Please enter no. of elements: '))
arr = list(map(int,input('Please enter arr elements: ').split()))

if len(arr) != n:
    print('enter correct no. of elements')

else:
    print(squre_sum_of_prime_numbers(arr))