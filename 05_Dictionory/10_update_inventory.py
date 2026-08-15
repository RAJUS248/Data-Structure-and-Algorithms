def update_inventory(inventory,updates):

    for iteam, quality in updates.items():
        if iteam in inventory:
            inventory[iteam] += quality

        else:
            inventory[iteam] = quality

    return inventory

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
updates = {"bananas": 10, "grapes": 15, "apples": 2}

print(update_inventory(inventory,updates))