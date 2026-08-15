def binary_string(s):

    c = s.count('1')

    ans = (c * (c-1))//2
    return ans

s = "11101"
print(binary_string(s))