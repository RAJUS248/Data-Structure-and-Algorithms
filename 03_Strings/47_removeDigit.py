def removeDigit(number, digit):
        
        res = []

        for i in range(len(number)):

            if number[i] == digit:
                slicing = number[:i] + number[i+1:]
                res.append(slicing)

        return max(res)

number = "1231"
digit = "1"
print(removeDigit(number,digit))