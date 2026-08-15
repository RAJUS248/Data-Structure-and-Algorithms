def swap(number1, number2):
    
    return number2,number1

item1 = input("enter 1st number: ") 
item2 = input("enter 2nd number: ")

item1,item2 = swap(item1,item2)

print(f"the item1 = {item1} and item2 = {item2} ")