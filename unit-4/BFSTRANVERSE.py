from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    # Add edge (directed or undirected based on need)
    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

        # Ensure all nodes appear
        if v not in self.adj:
            self.adj[v] = []

    # BFS Traversal
    def bfs(self, start):
        visited = set()
        queue = deque()
        result = []

        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result


# 🔹 Main Program
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for _ in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("Enter start node: ")

bfs_result = g.bfs(start)

print("\nBFS Traversal:", bfs_result)           