def connected_components_count(graph):
    visited = set()
    count = 0

    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    stack.append(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count



if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
        "j": [],
    }

    print("Connected Components Count:", connected_components_count(graph))  # Output: 1


    