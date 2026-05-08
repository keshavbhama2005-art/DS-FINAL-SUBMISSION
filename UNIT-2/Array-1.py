# arry ko display karana ka leya function
def display(arr):
    print("Updated Array:", arr)

# arry ma insert karana ka leya function
def insert(arr, pos, value):
    shifts = 0
    
    arr.append(0)  
    
    for i in range(len(arr) - 1, pos, -1):
        arr[i] = arr[i - 1]
        shifts += 1

    arr[pos] = value
    return shifts

#arry ma  sa element  delete karna ka leya function
def delete(arr, pos):
    shifts = 0
    
    for i in range(pos, len(arr) - 1):
        arr[i] = arr[i + 1]
        shifts += 1

    arr.pop()  # array ma sa last element ko remove karna ka leya
    return shifts

# input use for take input from user

arr = list(map(int, input("Enter elements (space-separated): ").split()))

print("\n1. Insert\n2. Delete")
choice = int(input("Enter choice: "))

if choice == 1:
    pos = int(input("Enter position (0 to {}): ".format(len(arr))))
    value = int(input("Enter value: "))
    
    shifts = insert(arr, pos, value)

elif choice == 2:
    pos = int(input("Enter position (0 to {}): ".format(len(arr)-1)))
    
    shifts = delete(arr, pos)


display(arr)

print("Shift Count:", shifts)

if shifts == 0:
    print("Time Complexity: O(1)")
else:
    print("Time Complexity: O(n)")