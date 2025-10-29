from collections import deque

def bfs(graph, start, n):
    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# --- Input Section ---
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

# Initialize graph as an adjacency list
graph = [[] for _ in range(n)]

print("Enter each edge as two space-separated nodes (e.g., 0 1):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # Omit this line if the graph is directed

start_node = int(input("Enter starting node: "))
print("BFS traversal from node", start_node, ":")
bfs(graph, start_node, n)

# Enter number of nodes: 5
# Enter number of edges: 6
# Enter each edge as two space-separated nodes (e.g., 0 1):
# 0 1
# 0 2
# 1 2
# 1 3
# 2 4
# 3 4
# Enter starting node: 0
# BFS traversal from node 0 :
# 0 1 2 3 4 