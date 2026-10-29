class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:

    def __init__(self):
        self.head = None

    def insert_at_end(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        if self.head.next is None:
            self.head.next = new_node
            return

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = new_node
        return

    def palindrome(self):

        lst = []
        cur = self.head

        while cur:
            lst.append(cur.data)
            cur = cur.next

        return lst == lst[::-1]
    
    def print_list(self):

        cur = self.head

        while cur:

            print(cur.data, end="->")
            cur = cur.next

        print("None")

sll = SLL()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(20)
sll.insert_at_end(10)

sll.print_list()
print(sll.palindrome())