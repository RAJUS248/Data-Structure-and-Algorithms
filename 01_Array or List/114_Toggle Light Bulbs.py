def toggleLightBulbs(bulbs):

    res = set()

    for num in bulbs:
        
        if num not in res:
            res.add(num)

        else:
            res.remove(num)

    return sorted(res)

bulbs = [10,30,20,10]
print(toggleLightBulbs(bulbs))