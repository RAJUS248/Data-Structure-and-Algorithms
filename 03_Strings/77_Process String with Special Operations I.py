def processStr(s):
        
        res = []

        for ch in s:

            if ch == "*" and res:
                res.pop()

            elif ch == "#":
                res = res * 2

            elif ch == "%":
                res.reverse()

            elif ch.isalpha():
                res.append(ch)

        return "".join(res)

s = "ztv#*l" #"d*#q%*" # "a#b%*"
print(processStr(s))

r = [1,2,3]
r = r * 2
print(r)


