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

    def mergeTwoList(self,list1,list2):

        lst = Node(0)
        tail = lst

        while list1 and list2:

            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1

        else:
            tail.next = list2

        return lst.next
             

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
sll.insert_at_end(70)
sll.print_list()

sll2 = SLL()
sll2.insert_at_end(20)
sll2.insert_at_end(30)
sll2.insert_at_end(50)
sll2.insert_at_end(60)
sll2.print_list()

mlst = SLL()
mlst.head = mlst.mergeTwoList(sll.head,sll2.head)
print("Merged: ", end="")
mlst.print_list()
