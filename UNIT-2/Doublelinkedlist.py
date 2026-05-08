class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Traverse and display
    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print("List:", result)

    # Insert value after the target value
    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = Node(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:  
                    temp.next.prev = new_node

                temp.next = new_node
                print(f"Inserted {x} after {target}")
                return

            temp = temp.next

        print("Target not found!")

    # Delete a given position at 0 index
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Case 1: delete the head node
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print("Deleted position 0")
            return

        # position ko Traverse karna ka leya
        for _ in range(pos):
            temp = temp.next
            if temp is None:
                print("Position out of range")
                return

        # pointers Update karna ka leya used 
        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print(f"Deleted position {pos}")


# example usage
dll = DoublyLinkedList()

# Initial list creation
dll.head = Node(10)
second = Node(20)
third = Node(30)

dll.head.next = second
second.prev = dll.head

second.next = third
third.prev = second

dll.display()

# Operations
dll.insert_after(20, 25)
dll.display()

dll.delete_at_position(2)
dll.display()