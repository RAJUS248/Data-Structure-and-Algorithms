def totalFruit(fruits):

    l = 0
    max_count = 0
    seen = {}  
  
    for r in range(len(fruits)):
 
        seen[fruits[r]] = seen.get(fruits[r],0) + 1

        if len(seen) > 2:
            max_count -= seen[fruits[l]]
            del seen[fruits[l]]
            l += 1
            max_count += 1
            

        else:
            max_count += 1

    return max_count
        

fruits = [1,2,3,2,2]
# print(totalFruit(fruits))




