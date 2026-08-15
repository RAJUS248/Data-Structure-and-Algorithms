def postfix(string):
    stack = []

    for ch in string:
        if ch.isdigit():
            stack.append(int(ch))

        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if ch == "+":
                stack.append(num2 + num1)

            elif ch == "-":
                stack.append(num2 - num1)

            elif ch == "*":
                stack.append(num2 * num1)

            elif ch == "/":
                stack.append(num2 / num1)

    return stack.pop()

string = "52+83-*4/"
print(postfix(string))