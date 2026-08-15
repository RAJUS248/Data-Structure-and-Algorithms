class Node:
    def __init__(self, data):
        self.data = data      # Data value
        self.next = None     # Pointer to next node

# Driver code
if __name__ == "__main__":
    # Create an array
    arr = [2, 5, 8, 7]

    # Create first node
    head = Node(arr[0])
    curr = head
    print(curr.data)

    for i in range(1,len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
        print(curr.data)

    curr = head

    while curr:
        print(curr.data,end = "->")
        curr = curr.next
    print("None")
    
    