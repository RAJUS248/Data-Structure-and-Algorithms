def plusOne(digits):
        
        res = 0

        for num in digits:

            res = res * 10 + num

        res = res + 1
        res_dig = []

        for num in str(res):
            res_dig.append(int(num))

        return res_dig 

arr = [1,2,3]
print(plusOne(arr))