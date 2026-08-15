class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_position(self,data,pos):
        new_node = Node(data)

        if pos <= 0:
            print("position is out of range")
            return
        
        if self.head is None:
            self.head = new_node
            return
        
        # pos 1 and list is not empty
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # pos 2 or more

        cur_node = self.head
        cur_pos = 1

        while cur_pos < pos -1 and cur_node is not None:
            cur_pos += 1
            cur_node = cur_node.next

        if cur_node is None:
            print("position is out of range")
            return
        
        # insert at end
        if cur_node.next is None:
            cur_node.next = new_node
            new_node.prev = cur_node
            return
        
        # insert at mid
        new_node.next = cur_node.next
        new_node.prev = cur_node
        cur_node.next = new_node
        

    def print_node(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end =" ⇄ ")
            current_node = current_node.next

        print(None)

dll = DLL()
dll.insert_at_position(10,1)
dll.insert_at_position(20,2)
dll.insert_at_position(30,3)
dll.insert_at_position(50,4)
dll.insert_at_position(40,4)
dll.insert_at_position(60,4)
dll.insert_at_position(70,7)
dll.print_node()

