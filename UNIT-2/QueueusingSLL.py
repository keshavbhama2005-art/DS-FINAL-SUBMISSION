#  makeing Node class 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class using head (front) and tail (rear)
class Queue:
    def __init__(self):
        self.head = None   # front
        self.tail = None   # rear

    # Enqueue operation (O(1))
    def enqueue(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        print(f"Enqueued: {data}")

    # Dequeue operation (O(1))
    def dequeue(self):
        if self.head is None:
            print("Queue Underflow!")
            return None

        removed = self.head.data
        self.head = self.head.next

        # If queue becomes empty
        if self.head is None:
            self.tail = None

        print(f"Dequeued: {removed}")
        return removed

    # Front operation
    def front(self):
        if self.head is None:
            print("Queue is empty!")
            return None
        return self.head.data

    # Display queue
    def display(self):
        temp = self.head
        if temp is None:
            print("Queue is empty")
            return

        print("Queue state:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")