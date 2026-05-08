


# 🎓 ✅ COMPLETE VIVA ANSWERS (ALL EXPERIMENTS)

---

# 🔹 Experiment 14: O(n²) Sorts (Bubble / Selection)

### 1. Stable vs Unstable?

* **Stable:** Keeps order of equal elements
  👉 Example: Bubble Sort ✅
* **Unstable:** Changes order
  👉 Example: Selection Sort ❌

---

### 2. In-place meaning?

* Sorting without extra memory
* Uses only original array
* Space = O(1)

---

### 3. Why O(n²) is slow?

* Uses nested loops
* Comparisons grow very fast
* Large input → very high operations

---

# 🔹 Experiment 15: Insertion Sort

### 1. Worst-case input?

* Reverse sorted list
* Example: `[9, 8, 7, 6, 5]`
* Maximum shifts required

---

### 2. Is insertion sort stable?

* ✅ Yes, stable
* Equal elements keep order

---

### 3. Space complexity?

* O(1) (in-place)

---

# 🔹 Experiment 16: Merge Sort

### 1. Why stable?

* While merging, left element is chosen first if equal
* Maintains original order

---

### 2. Why needs extra memory?

* Uses temporary arrays during merge
* Cannot work fully in-place

---

### 3. Use in external sorting?

* Used for large data (files on disk)
* Sort chunks → merge them
* Efficient for big datasets

---

# 🔹 Experiment 17: Quick Sort

### 1. Worst-case for quick sort?

* Already sorted or reverse sorted input
* When pivot is smallest/largest

---

### 2. Is quick sort stable?

* ❌ No, not stable
* Order of equal elements may change

---

### 3. Average time?

* O(n log n)

---

# 🔹 Experiment 18: Heap Sort

### 1. Why heap sort not stable?

* Swaps distant elements
* Equal elements change order

---

### 2. Heap vs BST for Top-K?

* Heap is better:

  * Faster (O(n log k))
  * Simpler
* BST needs balancing

---

### 3. Real priority queue use?

* CPU scheduling
* Dijkstra algorithm
* Task scheduling
* Event systems

---

# 🔹 Benchmark Harness

### 1. Why reverse is worst for insertion?

* Every element shifts fully
* Maximum operations → O(n²)

---

### 2. Why quick sort degrades on sorted input?

* Bad pivot (last element)
* Creates unbalanced partitions

---

### 3. Why merge sort is stable but uses memory?

* Stable due to ordered merging
* Uses extra arrays → O(n) space

---

# 🚀 FINAL QUICK REVISION (1 MINUTE)

| Algorithm | Time             | Stable | Space    |
| --------- | ---------------- | ------ | -------- |
| Bubble    | O(n²)            | ✅      | O(1)     |
| Selection | O(n²)            | ❌      | O(1)     |
| Insertion | O(n²), best O(n) | ✅      | O(1)     |
| Merge     | O(n log n)       | ✅      | O(n)     |
| Quick     | O(n log n) avg   | ❌      | O(log n) |
| Heap      | O(n log n)       | ❌      | O(1)     |

---

