# Directed Weighted Graph using Adjacency List

class Graph:
    def __init__(self):
        self.adj = {}   # dictionary

    # Add edge (u -> v with weight w)
    def add_edge(self, u, v, w):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, w))

        # Ensure v also appears in graph (even if no outgoing edges)
        if v not in self.adj:
            self.adj[v] = []

    # Print adjacency list
    def display(self):
        print("\nAdjacency List:")
        for node in self.adj:
            print(f"{node} -> ", end="")
            for (neighbor, weight) in self.adj[node]:
                print(f"({neighbor}, w={weight})", end=" ")
            print()


# 🔹 Main Program
g = Graph()

n = int(input("Enter number of edges: "))

print("Enter edges in format: source destination weight")

for _ in range(n):
    u, v, w = input().split()
    g.add_edge(u, v, int(w))

g.display()