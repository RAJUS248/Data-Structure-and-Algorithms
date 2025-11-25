def sum_two_num(s1,s2):

    i = len(s1)-1
    j = len(s2)-1
    carry = 0
    res = ""

    while i >= 0 or j >= 0 or carry:

        if i >= 0:
            num1 = int(s1[i])
            i -= 1
        else:
            num1 = 0
            

        if j >= 0:
            num2 = int(s2[j])
            j -= 1

        else:
            num2 = 0
        

        sums = num1 + num2 + carry

        carry = sums // 10

        res += str(sums % 10)

        
    final_res = "".join(res[::-1])

    return final_res.lstrip("0") or "0"


s1 = "2300"
s2 = "5400"
print(sum_two_num(s1,s2))