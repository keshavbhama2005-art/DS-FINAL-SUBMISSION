import heapq

# 🔹 Main Program
heap = []

n = int(input("Enter number of elements: "))
print("Enter elements (priorities):")

# Insert into heap
for _ in range(n):
    val = int(input())
    heapq.heappush(heap, val)
    print("Heap after insert:", heap)

# Peek (minimum)
if heap:
    print("\nPeek (min element):", heap[0])

# Extract elements
print("\nExtraction order (Priority Queue):")
while heap:
    val = heapq.heappop(heap)
    print("Extracted:", val)
    print("Heap now:", heap)