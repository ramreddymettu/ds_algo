def has_path(graph, start, end):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex == end:
            return True
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return False

def has_path_recursive(graph, start, end):
    if start == end:
        return True
    for neighbor in graph[start]:
        return has_path_recursive(graph, neighbor, end)
    return False

def has_path_bfs(graph, start, end):
    from collections import deque
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex == end:
            return True
        for neighbor in graph[vertex]:
            queue.append(neighbor)
    return False
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

    # Test the function
    print(has_path_bfs(graph, 'a', 'f'))  # Output: True
    print(has_path_bfs(graph, 'a', 'e'))  # Output: True
    print(has_path_bfs(graph, 'b', 'c'))  # Output: False