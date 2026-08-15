class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)


    def dequeue(self):
        if self.is_empty():
            print("the queue is empty there no item to remove")
            return None
        return self.queue.pop(0)


    def is_empty(self):
        return len(self.queue) == 0
    
    def reverse(self):
        rev_queue = []
        for num in range(len(self.queue)-1,-1,-1):
            rev_queue.append(self.queue[num])
        self.queue = rev_queue   # update the original queue
        print("Queue reversed successfully!")

    def reverse_recur(self):
        if self.is_empty():
            return
        
        # it will remove items
        items = self.dequeue()

        # it will call function again
        self.reverse_recur()

        # it will add the last item to first
        self.enqueue(items)

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()    

q.reverse()    # After reversing

q.display()

q.reverse_recur()
q.display()

