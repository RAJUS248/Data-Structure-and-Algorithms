def Find_the_fine(date,car,fine):

    total = 0

    for i in range(len(car)):
       

        if date % 2 == 0 and car[i] % 2 != 0:
            total += fine[i]

        elif date % 2 != 0 and car[i] % 2 == 0:
            total += fine[i]

    return total

date = 11
car = [2375, 7682, 2325, 2352]
fine = [250, 500, 350, 200]

print(Find_the_fine(date,car,fine))


# or

def Find_the_fine(date,car,fine):

    total = 0

    for i in range(len(car)):

        if date % 2 != car[i] % 2 :
            total += fine[i]

    return total

date = 10
car = [2375, 7682, 2325, 2352]
fine = [250, 500, 350, 200]

print(Find_the_fine(date,car,fine))

