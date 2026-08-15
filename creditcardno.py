"""n = input()

if len(n) == 16:
    print("Valid")
    
else:
    print("Invalid")"""

# valid code  5123-4567-8912-3456

def is_valid(card):

    clean_card = card.replace("-","")       # remove hyphens like 5123456789123456

    if clean_card[0] not in "456":          # must start with 4, 5, or 6
        return False
    
    if len(clean_card) != 16:               # must be 16 digits long
        return False
    
    if  not clean_card.isdigit():           # must contain only digits
        return False
    
    if "-" in card:                         # if '-' is used, check correct format
        parts = card.split('-')             # split into groups
        if len(parts) != 4:                 # must have 4 groups
            return False
        for part in parts:
            if len(part) != 4:              # each group must have 4 digits
                return False

    for i in range(len(clean_card) - 3):                     # check for 4 repeated digits
        if clean_card[i] == clean_card[i + 1] == clean_card[i + 2] == clean_card[i + 3]:
            return False
        
    return True

  # ----------- INPUT AND OUTPUT PART ------------
    
n = int(input())
for _ in range(n):
    card_number = input().strip()
    if is_valid(card_number):
        print("Valid")
    else:
        print("Invalid")