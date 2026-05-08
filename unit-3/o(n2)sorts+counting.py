def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps


# Example Inputs
random_list = [5, 2, 9, 1, 5, 6]
sorted_list = [1, 2, 3, 4, 5, 6]

# Run on random input
sorted_arr1, comp1, swap1 = bubble_sort(random_list.copy())

# Run on already sorted input
sorted_arr2, comp2, swap2 = bubble_sort(sorted_list.copy())

print("Random Input:")
print("Sorted:", sorted_arr1)
print("Comparisons:", comp1)
print("Swaps:", swap1)

print("\nAlready Sorted Input:")
print("Sorted:", sorted_arr2)
print("Comparisons:", comp2)
print("Swaps:", swap2)