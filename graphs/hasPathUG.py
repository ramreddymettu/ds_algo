def has_path(graph, start, end, visited=set()):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == end:
            return True
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return False


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


if __name__ == "__main__":
    # Example graph represented as an adjacency list
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n'],
    ]

    graph = build_graph(edges)
    print("Graph:", graph)
    #print("Has path from 'i' to 'm':", has_path(graph, 'i', 'm'))  # Output: True
    #print("Has path from 'i' to 'o':", has_path(graph, 'i', 'o'))  # Output: False
    print("Has path from 'i' to 'j':", has_path(graph, 'i', 'j'))  # Output: True

