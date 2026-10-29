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

    def mid_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print("mid node is:",slow.data)
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end = "->")
            curr = curr.next

        print("None")      

sll = SLL()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.insert_at_beginning(30)
sll.insert_at_beginning(40)
sll.insert_at_beginning(50)
sll.insert_at_beginning(60)
# sll.insert_at_beginning(70)
sll.print_list()
sll.mid_node()