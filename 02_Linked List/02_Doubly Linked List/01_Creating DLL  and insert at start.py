class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self): 
        self.head = None
 
    def insert_at_beginning(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def print_node(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end =" ⇄ ")
            current_node = current_node.next

        print(None)

dll = DLL()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
dll.insert_at_beginning(40)
dll.print_node()
