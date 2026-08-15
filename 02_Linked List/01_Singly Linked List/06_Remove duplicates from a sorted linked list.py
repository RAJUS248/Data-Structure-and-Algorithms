class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)

        # empty node
        if self.head is None:
            self.head = new_node
            return

        # for 1 node
        if self.head.next is None:
            self.head.next = new_node
            return
        
        # for 2 or more node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node
        return
    
    def remove_dublicates(self):
        cur_node = self.head

        while cur_node and cur_node.next:
            if cur_node.data == cur_node.next.data:
                cur_node.next = cur_node.next.next

            else:
                cur_node = cur_node.next
  
        return


    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data,end ="->")
            cur_node = cur_node.next

        print("None")

sll = SLL()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(30)
sll.insert_at_end(30)
sll.remove_dublicates()
sll.print_list()