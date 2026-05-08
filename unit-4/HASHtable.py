class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists

    # Hash function
    def hash_func(self, key):
        return key % self.size

    # Insert key-value
    def insert(self, key, value):
        index = self.hash_func(key)
        bucket = self.table[index]

        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise append (collision handled here)
        bucket.append((key, value))

    # Get value by key
    def get(self, key):
        index = self.hash_func(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    # Delete key
    def delete(self, key):
        index = self.hash_func(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    # Display table
    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            for k, v in bucket:
                print(f"({k}:{v})", end=" -> ")
            print("None")


# 🔹 Main Program
size = int(input("Enter hash table size: "))
ht = HashTable(size)

n = int(input("Enter number of key-value pairs: "))
print("Enter key value pairs:")

for _ in range(n):
    key, value = input().split()
    ht.insert(int(key), value)

ht.display()

# Get operation
key = int(input("\nEnter key to search: "))
result = ht.get(key)
print("Value:", result if result else "Not Found")

# Delete operation
key = int(input("Enter key to delete: "))
if ht.delete(key):
    print("Deleted successfully")
else:
    print("Key not found")

ht.display()