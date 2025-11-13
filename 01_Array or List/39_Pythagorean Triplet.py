def pythagoreanTriplet(arr):

    max_val = 1000
    seen = set(arr)


    for a in range(1,max_val+1):

        if  a not in seen:
            continue

        for b in range(a,max_val+1):

            if b not in seen:
                continue

            c_sqr = (a*a) + (b*b)
            c = int(c_sqr**0.5)

            if c in seen and c*c == c_sqr:
                return True
            
    return False

arr = [3, 2, 4, 6, 5]

print(pythagoreanTriplet(arr))