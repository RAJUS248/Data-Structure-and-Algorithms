def sequentialDigits(low, high):
        
        ref = "123456789"

        res = []

        for l in range(2,10):

            for start in range(10 - l):

                num = int(ref[start:start+l])

                if low <= num <= high:
                    res.append(num)

        return res
            
        
low = 100
high = 300
print(sequentialDigits(low,high))
