def is_balance(parent):
    stack = []

    map = {")":"(" , "}":"{" , "]":"["}

    for ch in parent:
        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":

            if stack == []:
                return "Not Balance"
            
            top = stack.pop()
            if top != map[ch]:
                return "Not Balance"


    return "Balance"

        

parent = "((("
print(is_balance(parent))
    


def is_balance_v2(parent):
    stack = []

    map = {")":"(" , "}":"{" , "]":"["}

    for ch in parent:
        if ch in map:

            if stack == []:
                return "Not Balance"
            
            top = stack.pop()
            if top != map[ch]:
                return "Not Balance"
        
        else:
            stack.append(ch)


    if stack == []:
        return "Balance"
    
    else:
        return "Not Balance"

        

parent = "()(){}"
print(is_balance_v2(parent))
    

def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in bracket_map.values():  # Opening brackets
            stack.append(ch)
        elif ch in bracket_map:  # Closing brackets
            if not stack or stack.pop() != bracket_map[ch]:
                return False
        else:
            # Invalid character (optional since input is guaranteed)
            return False

    return len(stack) == 0

s = "()"
print(isValid(s))