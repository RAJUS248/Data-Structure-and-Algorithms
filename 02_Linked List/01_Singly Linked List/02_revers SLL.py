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

    def reverse(self):
        prev = None
        cur_node = self.head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
        self.head = prev


    def print_list(self):
        cur_node = self.head

        while cur_node is not None:
            print(cur_node.data, end = "->")
            cur_node = cur_node.next

        print("None")

sll = SLL()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.insert_at_beginning(30)
sll.print_list()
sll.reverse()
sll.print_list()