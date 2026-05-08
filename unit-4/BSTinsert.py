class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Insert into BST
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

# Search in BST
def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Inorder Traversal (returns sorted list)
def inorder(root):
    if root is None:
        return []
    
    return inorder(root.left) + [root.data] + inorder(root.right)


# 🔹 Main Program
root = None

n = int(input("Enter number of elements: "))
print("Enter elements:")

for _ in range(n):
    key = int(input())
    root = insert(root, key)

# Inorder Output
result = inorder(root)
print("\nInorder Traversal (Sorted):", result)

# Search Operation
search_key = int(input("Enter key to search: "))

if search(root, search_key):
    print("Found")
else:
    print("Not Found")