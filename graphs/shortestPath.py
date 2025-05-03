from collections import deque
from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)  # Assuming undirected graph
    return graph

def shortest_path(edges, start, end):
    graph = build_graph(edges)
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current_node, dist = queue.popleft()
        if current_node == end:
            return dist
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(current_node)
                queue.append((neighbor, dist + 1))
    return -1 


if __name__ == "__main__":

    # Example graph represented as an adjacency list
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v'],
    ]

    graph = build_graph(edges)
    print("Graph:", graph)

    print("Shortest path from 'w' to 'z':", shortest_path(edges, 'w', 'z'))  # Output: 2
    print("Shortest path from 'x' to 'z':", shortest_path(edges, 'x', 'z'))  # Output: 3
    print("Shortest path from 'w' to 'x':", shortest_path(edges, 'w', 'x'))  # Output: 1
    print("Shortest path from 'x' to 'v':", shortest_path(edges, 'x', 'v'))  # Output: 2