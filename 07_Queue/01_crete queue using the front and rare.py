class Queue:
    def __init__(self,size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear
    
    def is_full(self):
        return self.rear == self.size - 1
    
    def enqueue(self,item):
        if self.is_full():
            print("Queue is full — cannot enqueue", item)
            return
        
        if self.front == -1:  # first eliment
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = item
        print("added",item)

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        
        remove = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        print("removed",remove)

    def display(self):
        print("Queue",self.queue)
        print(f"Front → {self.front}, Rear → {self.rear}")

q = Queue(5)
print(q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.dequeue()
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print(q.is_full())
q.display()
