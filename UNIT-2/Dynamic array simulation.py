class DynamicArray:
    def __init__(self):
        self.capacity = 1   
        self.size = 0       
        self.arr = [None] * self.capacity

    def append(self, value):
    
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.arr[self.size] = value
        self.size += 1
        print(f"Appended {value} -> Size: {self.size}, Capacity: {self.capacity}")

    def pop(self):
        if self.size == 0:
            print("Array is empty. Cannot pop.")
            return None

        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1

        print(f"Popped {value} -> Size: {self.size}, Capacity: {self.capacity}")
        return value

    def _resize(self, new_capacity):
        print(f"Resizing from {self.capacity} to {new_capacity}")
        new_arr = [None] * new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

da = DynamicArray()


operations = [
    ("append", 10),
    ("append", 20),
    ("append", 30),
    ("append", 40),
    ("pop", None),
    ("append", 50),
    ("append", 60),
]

for op, val in operations:
    if op == "append":
        da.append(val)
    elif op == "pop":
        da.pop()