def fibonacci(number):

    if number <= 1:
        return number
    
    return fibonacci(number - 1) + fibonacci(number - 2)

number = 45

print(fibonacci(number))

# for i in range(number):
#     print(fibonacci(i), end = "")


# def fibonacci_v2(number):

#     if number <= 1:
#         return number
    
#     a,b = 0,1

#     for _ in range(number-1):
#         a,b = b,a+b

#     return b

# number = 7
# print("\n",fibonacci_v2(number))
