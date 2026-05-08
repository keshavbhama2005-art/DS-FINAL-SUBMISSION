import random
import time

# ---------- Sorting Algorithms ----------

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# ---------- Dataset Generator ----------

def generate_data(size, seed):
    random.seed(seed)
    base = [random.randint(1, 10000) for _ in range(size)]

    return {
        "Random": base,
        "Sorted": sorted(base),
        "Reverse": sorted(base, reverse=True)
    }


# ---------- Timing Function ----------

def measure_time(func, data):
    start = time.perf_counter()
    func(data.copy())  # IMPORTANT: copy input
    end = time.perf_counter()
    return round(end - start, 6)


# ---------- Benchmark ----------

def run_benchmark():
    sizes = [1000, 5000, 10000]
    seed = 42

    algorithms = {
        "Insertion": insertion_sort,
        "Merge": merge_sort,
        "Quick": quick_sort
    }

    print("\nTiming Table (seconds)\n")
    print(f"{'Size':<8} {'Type':<10} {'Insertion':<12} {'Merge':<12} {'Quick':<12}")
    print("-" * 60)

    for size in sizes:
        datasets = generate_data(size, seed)

        for dtype, data in datasets.items():
            t1 = measure_time(insertion_sort, data)
            t2 = measure_time(merge_sort, data)
            t3 = measure_time(quick_sort, data)

            print(f"{size:<8} {dtype:<10} {t1:<12} {t2:<12} {t3:<12}")


# Run benchmark
run_benchmark()