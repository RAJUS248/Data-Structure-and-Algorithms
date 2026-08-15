class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size
    
    def enqueue(self,item):
        if self.is_full():
            print("queue is full")
            return
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        
        remove = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.count -= 1
        print("removed",remove)

    def display(self):
        print("circuler queue: ",self.queue)

# --- Test the Circular Queue ---
q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()       # Output: 10 20 30

q.dequeue()       # Removes 10
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)     # Should say “Queue is full”
q.display()       # Output: 20 30 40 50