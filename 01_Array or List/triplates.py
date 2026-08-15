def get_difference_of_avr_of_even_and_odd(numbers)->int:

    odd_sum = 0
    even_sum = 0

    odd_count = 0
    even_count = 0

    for num in numbers:

        if num % 2 == 0:
            even_sum += num
            even_count += 1

        else:
            odd_sum += num
            odd_count += 1

    if odd_count == 0:
        odd_avg = 0

    else:
        odd_avg = odd_sum / odd_count


    if even_count == 0:
        even_avg = 0

    else:
        even_avg = even_sum / even_count

    if odd_avg == even_avg:
        differnce = 0

    elif odd_avg > even_avg :
        differnce = odd_avg - even_avg
    
    else:
        differnce = even_avg - odd_avg
    
    return differnce


numbers = [22,3,6,15,8,3,7]
print(get_difference_of_avr_of_even_and_odd(numbers))
