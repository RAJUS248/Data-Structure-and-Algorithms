def find_shop(favorite_flavors,all_shops):
    
    flavors_set = set(favorite_flavors)

    for i in range(len(all_shops)):

        shop = set(all_shops[i])
        if flavors_set.issubset(shop):
            return i
    
    return None
        
    
# The 9 flavors the boy wants
favorite_flavors = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Each list is a shop, containing the flavor IDs it has.
all_shops = [   
                [1, 2, 3, 10, 11], 
                [4, 5, 7, 9, 10, 1, 2], 
                [9, 6, 4, 7, 1, 2, 3, 5, 8, 12, 13],
                [1, 2, 3, 4, 5, 6, 7, 8, 14],
                [8, 9, 4, 5, 6, 7, 1, 2, 3, 15]
            ]

print(find_shop(favorite_flavors,all_shops))