class Stack:
    def __init__(self):
        self.stack = []   # Each object has its own stack list

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        print(f"{item} is pushed")

    def peek(self):
        if self.is_empty():          # ✅ use your own method
            print("Error: Stack is empty")
            return None
        print(f"{self.stack[-1]} is peek")

    def pop(self):
        if self.is_empty():
            print("Error: Stack is empty")
            return None
        print(f"{self.stack.pop()} popped")

    def display(self):
        print("Stack:", self.stack)


# Usage
s = Stack()
s.push(10)
s.push(20)
s.display()
s.peek()
s.pop()
s.display()


"""
class Stack:

    
    @staticmethod
    def is_empty(stack):
        return len(stack) == 0
    
    @staticmethod
    def push(stack,item):
        push = stack.append(item)
        print(f"the {push} is push ")

    @staticmethod
    def peek(stack):
        if stack is None:
            return "stack is empty"
        
        peek = stack[-1]
        print(f"peek is {peek}")


    @staticmethod
    def pop(stack):
        if stack is None:
            return "stack is empty"
        
        pop = stack.pop()
        print(f"pop is {pop}")


    @staticmethod
    def display(stack):
        print(stack)

    
stack = []
s = Stack()
s.is_empty(stack)
s.push(stack,10)
s.push(stack,20)
s.display(stack)
s.peek(stack)
s.pop(stack)
s.display(stack)
Stack.display(stack)

"""