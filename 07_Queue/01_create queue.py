def enqueue(item):
    queue.append(item)

def is_empty():
    return len(queue) == 0

def dequeue():
    if is_empty():
        print("the queue is empty there is no poping items")
        return None

    
    print("removed",queue.pop(0))

def display():
    print(queue)


queue = []

if __name__ == "__main__":
    print(is_empty())
    enqueue(10)
    enqueue(20)
    enqueue(40)

    display() 

    dequeue()
    dequeue()
    dequeue()
    dequeue()
    display()
   
   