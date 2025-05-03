def dfs(graph, start):
    stack = [start]
    while stack:
        vertex = stack.pop()
        print(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

def dfs_recursive(graph, start):
    print(start)
    for neighbor in graph[start]:
        dfs_recursive(graph, neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

if __name__ == "__main__":
    print("DFS Traversal:")
    dfs_recursive(graph, 'a')

