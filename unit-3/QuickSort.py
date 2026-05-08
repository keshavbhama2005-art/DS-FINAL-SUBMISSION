def partition(arr, low, high):
    pivot = arr[high]  # last element as pivot
    i = low - 1        # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # sort left and right parts
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example
arr = [10, 7, 8, 9, 1, 5]

print("Original:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted:", arr)