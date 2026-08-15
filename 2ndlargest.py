def second_largest(arr):

    if len(arr) < 2:
        return None
    

    largest = seclargest = float('-inf')

    for number in arr:
        if number > largest:
            seclargest = largest
            largest = number

        elif number > seclargest and number != largest:
            seclargest = number

    if seclargest == float('-inf'):
            return None
    return seclargest
    
arr = [8,8]

result = second_largest(arr)

print("secend largest is ",result)


# small example 

max_val = float('-inf')

for num in [5, 10, 3]:
    if num > max_val:
        max_val = num

print("Maximum is:", max_val)

