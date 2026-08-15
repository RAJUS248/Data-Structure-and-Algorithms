def wateringPlants(plants, capacity):
    
    n = len(plants)
    water = capacity
    step = 0

    for i in range(n):
        if water < plants[i]:
            step += 2 * i 
            water = capacity

        step += 1
        water -= plants[i]
        

    return step

plants = [2,2,3,3]
capacity = 5
print(wateringPlants(plants,capacity))