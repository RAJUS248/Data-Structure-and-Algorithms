def stack_palindrome(string):
    stack = []
    reverse_str = ""

    for ch in string:
        stack.append(ch)

    while stack:

        reverse_str += stack.pop()

    if string == reverse_str:
        return "Palindrome"
    
    else:
        return "Not Palindrome"

string = "baa"
print(stack_palindrome(string)) 