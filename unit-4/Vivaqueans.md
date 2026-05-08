
# 🔥 ✅ THEORY VIVA ANSWERS (Experiment 20–28)

---

# 🔹 **Experiment 20: BST (Insert/Search/Inorder)**

### 1️⃣ Why inorder traversal gives sorted output?

In a BST, all values in the **left subtree are smaller** than the root and all values in the **right subtree are larger**.
Inorder traversal follows **Left → Root → Right**, so elements are visited in **ascending order**, producing a sorted list.

---

### 2️⃣ Worst-case BST height?

Worst case occurs when the BST becomes **skewed (like a linked list)**.
Height = **n (number of nodes)**
Time complexity becomes **O(n)**.

---

### 3️⃣ Average complexity?

For a balanced BST:

* Insert → **O(log n)**
* Search → **O(log n)**
* Inorder → **O(n)**

---

# 🔹 **Experiment 21: BST Delete**

### 1️⃣ Inorder successor meaning?

The **inorder successor** is the **smallest element in the right subtree** of a node.
Used when deleting a node with **two children**.

---

### 2️⃣ Why delete is tricky?

Because we must maintain BST structure while handling **three cases**:

* Leaf node
* One child
* Two children

Each case requires a different approach.

---

### 3️⃣ How to verify correctness?

Perform **inorder traversal**.
If output is **sorted**, BST is correct.
Also verify: **Left < Root < Right property**.

---

# 🔹 **Experiment 22: Heap / Priority Queue**

### 1️⃣ Why heap for priority queues?

Heap allows:

* Fast access to **highest/lowest priority element**
* Efficient insert and delete operations
* Maintains partial order automatically

---

### 2️⃣ Insert / Extract complexity?

* Insert → **O(log n)**
* Extract → **O(log n)**
* Peek → **O(1)**

---

### 3️⃣ Where used in industry?

* CPU scheduling
* Dijkstra’s algorithm
* Task scheduling systems
* Network packet handling

---

# 🔹 **Experiment 23: Graph (Adjacency List)**

### 1️⃣ List vs Matrix?

* **Adjacency List** → Space efficient (O(V+E)), good for sparse graphs
* **Adjacency Matrix** → Fast lookup (O(1)), but uses O(V²) space

---

### 2️⃣ Directed vs Undirected?

* Directed → edges have **direction (u → v)**
* Undirected → edges are **bidirectional (u ↔ v)**

---

### 3️⃣ Weighted graph use?

Used when edges have **cost/distance/time**, e.g.:

* Maps (Google Maps)
* Network routing
* Transport systems

---

# 🔹 **Experiment 24: BFS**

### 1️⃣ Why queue in BFS?

Queue follows **FIFO (First In First Out)**.
Ensures nodes are visited **level by level**.

---

### 2️⃣ Shortest path relation?

BFS gives **shortest path in unweighted graphs** because it explores nodes in increasing distance order.

---

### 3️⃣ Complexity O(V+E)?

* Each vertex visited once → **O(V)**
* Each edge explored once → **O(E)**
  Total = **O(V + E)**

---

# 🔹 **Experiment 25: DFS**

### 1️⃣ DFS vs BFS?

* DFS → depth-wise traversal (uses stack/recursion)
* BFS → level-wise traversal (uses queue)
* BFS finds shortest path, DFS does not guarantee

---

### 2️⃣ Recursion depth issue?

DFS may go very deep in large graphs, causing **stack overflow**.
Solution:

* Use iterative DFS (stack)
* Increase recursion limit

---

### 3️⃣ Use case of DFS?

* Cycle detection
* Topological sorting
* Backtracking problems
* Connected components

---

# 🔹 **Experiment 26: Hash Table**

### 1️⃣ Collision meaning?

When **multiple keys map to the same index** in a hash table.

---

### 2️⃣ Why chaining works?

Each index stores a **list of elements**, so multiple keys can be stored without overwriting.

---

### 3️⃣ Load factor?

Load Factor = **number of elements / table size**
Indicates how full the hash table is.
Higher load factor → more collisions.

---

# 🔹 **Experiment 27: Trie**

### 1️⃣ Trie vs hash map for prefix?

* Trie → efficient prefix search (**O(L)**)
* Hash map → not efficient for prefixes

---

### 2️⃣ Space trade-off?

Trie uses **more memory** because each character is stored as a node.
Trade-off: faster prefix operations vs higher space usage.

---

### 3️⃣ Autocomplete use?

Used in:

* Search engines
* Mobile keyboards
* Spell checkers
* Dictionary apps

---

# 🔹 **Experiment 28: Bloom Filter**

### 1️⃣ Can Bloom Filter have false negatives?

❌ No
If it says “not present”, it is always correct.
Only false positives are possible.

---
