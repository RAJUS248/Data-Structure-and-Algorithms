def isNumber(numbers:int):
    isInteger = True

    for eachNumber in numbers:
        if eachNumber >= '0' and eachNumber <= '9':
            continue

        else:
            isInteger = False

    return isInteger

numbers = '12365'

result = isNumber(numbers)

if result:
    print("This is the number")

else:
    print("it is not an number")



def isNum(nums):

    for eachnum in nums:
        if eachnum < '0' or eachnum > '9':

            return False
    return True

nums = '12B65'

result = isNum(nums)

if result:
    print("This is the number")

else:
    print("it is not an number")
