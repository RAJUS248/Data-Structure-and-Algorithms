
# Checks if the stack is empty.

def is_empty(stack):
    return len(stack) == 0

# Push Operation

def push(stack,item):
    stack.append(item)
    print(f"the {item} is pushed in stack")

# peek operation

def peek(stack):

    if is_empty(stack):
        print("Error: Cannot peek at an empty stack.")
        return None
    
    peek = stack[-1]

    print(f"the peek value is {peek}")

# display

def display(stack):
    if stack:
        print("the stack is: ",stack)

    else:
        print("stack is empty")


# pop operation

def pop(stack):
    if is_empty(stack):
        print("Error: Cannot pop from an empty stack.")
        return None
    
    pop = stack.pop()
    print(f"the {pop} is poped")

if __name__ == "__main__":

    # Initialize an empty stack (global or passed as argument)

    stack = []

    # empty
    print("stack is empty: ",is_empty(stack))


    # Push
    push(stack,10)
    push(stack,20)
    push(stack,30)
    push(stack,40)
    push(stack,50)
    push(stack,60)

    # display Stack

    display(stack)

    # peek
    peek(stack)
    
    # pop
    pop(stack)
    display(stack)
    peek(stack)

    
