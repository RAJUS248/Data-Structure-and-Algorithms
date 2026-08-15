class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
    
        return not (self.stack1 or self.stack2)
        

    def enqueue(self,item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:  # Queue is empty
            print("Queue is empty — nothing to dequeue.")
            return None
        
        return self.stack2.pop()
    
    def display(self):
        queue = self.stack2[::-1] + self.stack1
        print(queue)

q = QueueUsingStack()

print(q.is_empty())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.enqueue(50)



q.display()