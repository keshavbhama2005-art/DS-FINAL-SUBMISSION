class Graph:
    def __init__(self):
        self.adj = {}

    # Add edge (directed)
    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

        # Ensure all nodes appear
        if v not in self.adj:
            self.adj[v] = []

    # DFS Helper
    def dfs_util(self, node, visited, result):
        visited.add(node)
        result.append(node)

        for neighbor in self.adj[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, result)

    # DFS Traversal
    def dfs(self, start):
        visited = set()
        result = []
        self.dfs_util(start, visited, result)
        return result


# 🔹 Main Program
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for _ in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("Enter start node: ")

dfs_result = g.dfs(start)

print("\nDFS Traversal:", dfs_result)