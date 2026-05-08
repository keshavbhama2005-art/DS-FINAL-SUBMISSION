# Experiment 8: 2D Arrays (Matrix Traversal + Operations)

# make function for take input from user for 2D array (matrix)
def input_matrix(rows, cols):
    matrix = []
    print("Enter matrix elements row-wise:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return matrix


# Function ko display karana ka leyad  display matrix used
def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Row sum used for calculate sum of each row
def row_sum(matrix):
    print("\nRow-wise Sum:")
    for i in range(len(matrix)):
        print(f"Row {i+1} sum = {sum(matrix[i])}")


# Column sum used for calculate sum of each column
def col_sum(matrix):
    print("\nColumn-wise Sum:")
    cols = len(matrix[0])
    for j in range(cols):
        s = 0
        for i in range(len(matrix)):
            s += matrix[i][j]
        print(f"Column {j+1} sum = {s}")


# Search for a value in matrix and return its position
def search(matrix, key):
    found = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == key:
                print(f"\nValue {key} found at position (Row {i+1}, Column {j+1})")
                found = True
    if not found:
        print(f"\nValue {key} not found in matrix")


#  matrix ka Transpose karna ka leya used this function of matrix
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    trans = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        trans.append(row)

    print("\nTranspose Matrix:")
    display_matrix(trans)


# output program
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = input_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

row_sum(matrix)
col_sum(matrix)

key = int(input("\nEnter value to search: "))
search(matrix, key)

transpose(matrix)