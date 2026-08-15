class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node
        
            
        

    def print_node(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end =" ⇄ ")
            current_node = current_node.next

        print(None)

dll = DLL()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.print_node()