def minimumRefill(plants, capacityA, capacityB):

    l = 0
    r = len(plants) - 1

    count = 0

    waterA = capacityA
    waterB = capacityB

    while l < r:
        if waterA < plants[l]:
            waterA = capacityA
            count += 1

        waterA -= plants[l]
   
        l += 1

        if waterB < plants[r]:
            waterB = capacityB
            count += 1

        waterB -= plants[r]

        r -= 1

    if l == r:

        if waterA >= waterB:

            if waterA < plants[l]:
                count +=1

        else:
            if waterB < plants[r]:
                count +=1

    return count

plants = [1,2,4,4,5]
capacityA = 6
capacityB = 5
print(minimumRefill(plants,capacityA,capacityB))