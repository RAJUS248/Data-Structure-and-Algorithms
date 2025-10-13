class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
 
    def push(self,data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.count += 1
        print(f"the value {data} is pushed in stack")
        

    def pop(self):
        if self.top is None:
            print("stack is empty")
            return
        
        popped_value = self.top.data
        self.top = self.top.next
        self.count -= 1
        print("popped value is :", popped_value)
        return popped_value
    
    def peek(self):
        if self.top is None:
            return None
        print("peek is: ",self.top.data)
        return self.top.data
    
    def get_count(self):
        print("the count:",self.count)
        return self.count
    
    def display(self):

        if self.top is None:
            print("stack is empty")
            return
        
        current_top = self.top
        while current_top:
            print(current_top.data, end = " -> ")
            current_top = current_top.next

        print("None")

if __name__ == "__main__":
    stack = Stack()
    stack.display()
    stack.push(1)
    stack.display()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()
    stack.get_count()
    stack.pop()

    stack.display()
    stack.peek()

    stack.get_count()
