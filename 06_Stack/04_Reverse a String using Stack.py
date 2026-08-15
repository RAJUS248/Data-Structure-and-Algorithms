# using stack

string2 = "hello"
stack1 = []

for ch in string2:
    stack1.append(ch)

rev_string = ""
while stack1:

    rev_string += stack1.pop()

print(rev_string)


# not using stack
string = "hello"
stack = []

for ch in range(len(string)-1,-1,-1):
    stack.append(string[ch])

print("".join(stack))


# not using stack

string1 = "hello"
for i in range(len(string1)-1,-1,-1):
    print(string1[i],end = "")


