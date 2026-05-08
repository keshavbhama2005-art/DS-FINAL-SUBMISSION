def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted lists
    while i < len(left) and j < len(right):
        # <= ensures stability
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Example
arr = [5, 2, 9, 1, 5, 6]

sorted_arr = merge_sort(arr)

print("Original:", arr)
print("Sorted:", sorted_arr)