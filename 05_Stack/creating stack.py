class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        

    def push(self,data): 
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("stack is empty")
            return
        
        popped_value = self.top.data        # put top value data in popped value
        self.top = self.top.next            # top value become below the top means    3 below 2 is top now
        print("poping value: ",popped_value)                 
        return popped_value                 
        
    def peek(self):
        if self.top is None:
            return None
        print("peek value :",self.top.data)
        return self.top.data

    def is_empty(self):
        return self.top is None
    
    def display(self):
        current_node = self.top

        while current_node:
            print(current_node.data, end = " -> ")
            current_node = current_node.next

        print("None")

stack = Stack()

stack.is_empty()
stack.push(1)
stack.push(2)
stack.push(3)

stack.display()
stack.pop()
stack.peek()
stack.display()

         
            
        
       

        

    
