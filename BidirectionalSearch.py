from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front_visited = {start: None}
    back_visited = {goal: None}
    front_queue, back_queue = deque([start]), deque([goal])

    while front_queue and back_queue:
        # Expand forward
        f_node = front_queue.popleft()
        for neighbor in graph[f_node]:
            if neighbor not in front_visited:
                front_visited[neighbor] = f_node
                front_queue.append(neighbor)
                if neighbor in back_visited:
                    print(f"Intersection at: {neighbor}")
                    return build_path(front_visited, back_visited, neighbor)

        # Expand backward
        b_node = back_queue.popleft()
        for neighbor in graph[b_node]:
            if neighbor not in back_visited:
                back_visited[neighbor] = b_node
                back_queue.append(neighbor)
                if neighbor in front_visited:
                    print(f"Intersection at: {neighbor}")
                    return build_path(front_visited, back_visited, neighbor)
    return None

def build_path(front, back, meet):
    path = []
    node = meet
    while node is not None:
        path.append(node)
        node = front[node]
    path.reverse()
    node = back[meet]
    while node is not None:
        path.append(node)
        node = back[node]
    return path

# --- Input Section ---
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))
graph = {i: [] for i in range(n)}

print("Enter each edge as two space-separated nodes (e.g., 0 1):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))

path = bidirectional_search(graph, start, goal)
print("Optimal path:" if path else "No path found")
if path:
    print(*path)

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
# PS D:\exp> python BidirectionalSearch.py
# Enter number of nodes: 15
# Enter number of edges: 14
# Enter each edge as two space-separated nodes (e.g., 0 1):
# 0 4
# 1 4
# 2 5
# 3 5
# 4 6
# 5 6
# 6 7
# 7 8
# 8 9
# 8 10
# 9 11
# 9 12
# 10 13
# 10 14
# Enter starting node: 0
# Enter goal node: 14
# Intersection at: 7
# Optimal path:
# 0 4 6 7 8 10 14

        # 0       1       2       3
        #  \     /         \     /
        #    \   /           \   /
        #      4               5
        #       \             /
        #        \           /
        #          \       /
        #            6
        #            |
        #            7
        #            |
        #            8
        #           / \
        #          9   10
        #         / \   / \
        #        11 12 13 14
