class BloomFilter:
    def __init__(self, size, k):
        self.size = size
        self.k = k
        self.bit_array = [0] * size

    # Simple hash functions
    def hash_funcs(self, item):
        results = []
        for i in range(self.k):
            hash_val = hash(item + str(i)) % self.size
            results.append(hash_val)
        return results

    # Insert item
    def insert(self, item):
        for pos in self.hash_funcs(item):
            self.bit_array[pos] = 1

    # Check membership
    def check(self, item):
        for pos in self.hash_funcs(item):
            if self.bit_array[pos] == 0:
                return "Definitely Not Present"
        return "Possibly Present"

    # Display bit array
    def display(self):
        print("Bit Array:", self.bit_array)


# 🔹 Main Program
size = int(input("Enter size of Bloom Filter: "))
k = int(input("Enter number of hash functions: "))

bf = BloomFilter(size, k)

n = int(input("Enter number of items to insert: "))
print("Enter items:")

for _ in range(n):
    item = input().strip()
    bf.insert(item)

bf.display()

q = int(input("\nEnter number of queries: "))

for _ in range(q):
    item = input("Enter item to check: ")
    print(item, "->", bf.check(item))
    