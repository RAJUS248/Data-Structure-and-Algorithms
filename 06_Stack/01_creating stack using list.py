# creating/ pushing stack 

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)

# peek

peek = stack[-1]
print(peek)

# pop
stack.pop()
print(stack)
print("end \n \n")
# Empty

if len(stack) == 0:
    print("Stack is empty")


# --------------------  Syastmatic way ----------------------- #

# creating/ pushing stack 

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

print("the stack: ",stack)

# peek

if stack:
    peek = stack[-1]

    print("the peek is: ", peek)


# pop

if stack:
    pop = stack.pop()
    print("pop iteam is: ",pop)
    print("after Pop: ", stack)


# Empty

is_empty = len(stack) == 0
print("stack is empty", is_empty)


