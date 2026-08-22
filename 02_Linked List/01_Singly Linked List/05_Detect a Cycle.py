class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
  
    def insert_at_end(self,data):
        new_node = Node(data)

        # for empty node
        if self.head is None:
            self.head = new_node
            return
        
        # for 1 node
        if self.head.next is None:
            self.head.next = new_node
            return
        
        # 2 or more node
        cur_node = self.head

        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node
        return
    
    def detect_cycle(self):
        fast = self.head
        slow = self.head

        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                print("cycle")
                return True
            
        print("no")
        return False

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data, end = "->")
            cur_node = cur_node.next

        print(None)

    def print_cycle(self,limit = 100):
        cur_node = self.head
        count = 0
        while cur_node and count < limit:
            print(cur_node.data, end = "->")
            cur_node = cur_node.next
            count += 1
        print("----")

sll = SLL()

sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(40)
sll.insert_at_end(50)
sll.head.next.next.next.next.next = sll.head.next

sll.print_cycle()
sll.detect_cycle()
