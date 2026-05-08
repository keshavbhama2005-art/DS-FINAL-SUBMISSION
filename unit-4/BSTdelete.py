class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Insert
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Find inorder successor (min value in right subtree)
def find_min(node):
    while node.left:
        node = node.left
    return node

# Delete node
def delete_node(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)

    elif key > root.data:
        root.right = delete_node(root.right, key)

    else:
        # Case 1: No child (leaf)
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Two children
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete_node(root.right, successor.data)

    return root

# Inorder traversal
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


# 🔹 Main Program
root = None

n = int(input("Enter number of elements: "))
print("Enter elements:")

for _ in range(n):
    root = insert(root, int(input()))

print("\nInitial Inorder:", inorder(root))

d = int(input("\nEnter number of deletions: "))

for _ in range(d):
    key = int(input("Enter key to delete: "))
    root = delete_node(root, key)
    print("Inorder after deleting", key, ":", inorder(root))