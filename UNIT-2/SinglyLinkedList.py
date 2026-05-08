
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

   
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Value not found")

    # Traverse (display list)
    def traverse(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



sll = SinglyLinkedList()

sll.insert_at_beginning(10)
sll.traverse()

sll.insert_at_beginning(5)
sll.traverse()

sll.insert_at_end(20)
sll.traverse()

sll.insert_at_end(30)
sll.traverse()

sll.delete_by_value(5) 
sll.traverse()

sll.delete_by_value(20)  
sll.traverse()

sll.delete_by_value(30)  
sll.traverse()

sll.delete_by_value(100) 
sll.traverse()