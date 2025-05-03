from collections import deque

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            queue.append(neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

if __name__ == "__main__":
    print("BFS Traversal:")
    bfs(graph, 'a')