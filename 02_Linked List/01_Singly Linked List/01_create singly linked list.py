class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class SLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        # empty 
        if self.head is None:
            self.head = new_node
            return

        # 1 node
        if self.head.next is None:
            self.head.next = new_node
            return
    
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node
        return
    
    def insert_at_position(self, position,data):
        # invalid position
        if position < 1:
            print("invalid position")
            return
        
        # at position 1 
       
        if position == 1:
            self.insert_at_beginning(data)
            return
        
        # more then 2 node
        new_node = Node(data)
        cur_node = self.head
        cur_pos = 1

        while cur_pos < position -1 and cur_node is not None:
            cur_node = cur_node.next
            cur_pos += 1

        # out of position
        if cur_node is None:
            print("invalid position out of range")
            return

        new_node.next = cur_node.next
        cur_node.next = new_node

    def print_nodes(self):
        cur_node = self.head
        
        while cur_node is not None:
            print(cur_node.data, end = "->")
            cur_node = cur_node.next

        print("None")

sll = SLL()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.print_nodes()
sll.insert_at_position(1,50)
sll.insert_at_position(2,30)
sll.insert_at_position(3,40)
sll.insert_at_position(10,10)
sll.insert_at_position(-1,10)
sll.print_nodes()


sll1 = SLL()
sll1.insert_at_end(10)
sll1.insert_at_end(20)
sll1.print_nodes()

