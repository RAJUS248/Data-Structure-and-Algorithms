def largestOddNumber(num):  

    for i in range(len(num)-1,-1,-1):

            if int(num[i]) % 2 != 0:

                return num[:i+1]

    return ""    

        # res = int(num)

        # while res > 0:

        #     if res % 2 != 0:
        #         return str(res)

        #     else:
        #         res //= 10

        # return ""

num = "4206"
print(largestOddNumber(num))