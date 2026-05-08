def insertion_sort(arr, show_passes=False):
    comparisons = 0
    shifts = 0  # instead of swaps, insertion sort shifts elements

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

        if show_passes:
            print(f"Pass {i}: {arr}")

    return arr, comparisons, shifts


# Example inputs
random_list = [8, 3, 5, 2, 9]
nearly_sorted = [1, 2, 3, 5, 4, 6]

print("Random Input:")
sorted_arr1, comp1, shift1 = insertion_sort(random_list.copy(), True)
print("Sorted:", sorted_arr1)
print("Comparisons:", comp1, "Shifts:", shift1)

print("\nNearly Sorted Input:")
sorted_arr2, comp2, shift2 = insertion_sort(nearly_sorted.copy(), True)
print("Sorted:", sorted_arr2)
print("Comparisons:", comp2, "Shifts:", shift2)