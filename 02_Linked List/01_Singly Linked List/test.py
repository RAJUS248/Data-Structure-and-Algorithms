class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class SLL:

    def __init__(self):
        self.head = None

    # insert_at_beginning
    def insert_at_beginning(self,data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = new_node

    def insert_at_position(self,data,pos):

        if pos < 1:
            print("Invalid Position")
            return
        
        if pos == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        count = 1
        cur =  self.head

        while cur is not None:

            if count == pos-1:
                new_node.next = cur.next
                cur.next = new_node
                return

            count += 1
            cur = cur.next

        print("Position out of range")


    def delete_at_begining(self):

        if self.head is None:
            print("There is no elements to delete")
            return

        self.head = self.head.next
        return

    def delete_at_end(self):

        if self.head is None:
            print("There is no elements to delete")
            return

        if self.head.next is None:
            self.head = None
            return

        cur = self.head

        while cur.next.next is not None:

            cur = cur.next

        cur.next = None

    def delete_at_position(self,pos):
        
        if self.head is None:
            print("There is no elements to delete")
            return
        
        if pos < 1:
            print("invalid position")
            return

        if pos == 1:
            self.delete_at_begining()
            return

        count = 1
        cur = self.head

        while cur:

            if count == pos-1:

                if cur.next is None:
                    print("the out of range")
                    return
                
                cur.next = cur.next.next
                return

            count += 1
            cur = cur.next

        print("the out of range")

    def search(self,key):

        cur = self.head

        while cur:

            if key == cur.data:
                print("key is found")
                return

            cur = cur.next

        print("key not found")

    def reverse(self):

        print("reverse")
        stack = []

        cur = self.head

        while cur.next is not None:

            stack.append(cur)
            cur = cur.next

        self.head = cur

        while stack:

            cur.next = stack.pop()
            cur = cur.next

        cur.next = None
        return self.head

    def find_mid(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        print(slow.data)

    def nth_from_end(self,n):
        toatl_lenth = 0

        cur = self.head

        while cur:
            toatl_lenth += 1
            cur = cur.next

        if n > toatl_lenth:
            print("n is out of length")
            return None

        nth = toatl_lenth - n

        cur = self.head

        while nth:

            cur = cur.next
            nth -= 1

        print(cur.data)
        return

    def remove_duplicate(self):

        cur = self.head
        seen = {cur.data}

        while cur.next:

            if cur.next.data not in seen:
                seen.add(cur.next.data)
                cur = cur.next

            else:
                cur.next = cur.next.next

        return
 

    def print_all(self):

        cur = self.head

        while cur:
            print(cur.data,end="->")
            cur = cur.next

        print("None")

sll = SLL()
sll.insert_at_beginning(30)
sll.insert_at_beginning(20)
sll.insert_at_beginning(30)
sll.insert_at_beginning(40)
sll.insert_at_beginning(30)
sll.insert_at_beginning(60)
sll.remove_duplicate()
sll.nth_from_end(7)
sll.print_all()
sll.find_mid()
sll.reverse()
sll.print_all()

sll.insert_at_end(5)
sll.print_all()

sll.insert_at_position(40,1)
sll.print_all()

sll.delete_at_begining()
sll.print_all()

sll.delete_at_end()
sll.print_all()

sll.delete_at_position(2)
sll.print_all()

sll.search(40)
