def isNumber(number):
    isInteger = True

    for char in number:
        if char >= '0' and char <= '9':
            continue
        else:
            isInteger = False

    return isInteger

number = '123B'

result = isNumber(number)

if result:
    print("is number")

else:
    print("not a number")
