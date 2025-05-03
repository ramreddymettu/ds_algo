def largest_component(graph):
    visited = set()
    largest_size = 0

    def dfs(node):
        stack = [node]
        size = 0
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                size += 1
                for neighbor in graph[current]:
                    stack.append(neighbor)
        return size

    for node in graph:
        if node not in visited:
            component_size = dfs(node)
            largest_size = max(largest_size, component_size)

    return largest_size


if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    print("Largest Component Size:", largest_component(graph))  # Output: 4