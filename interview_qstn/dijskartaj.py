## Tekion Interview 
import heapq

def dijkstra_min_path(grid):
    
    if not grid or not grid[0]:
        return 0, [] 
    
    m, n = len(grid), len(grid[0])
    start = (0, 0)
    end = (m - 1, n - 1)

    heap = [(grid[0][0], 0, 0 )]
    costd = {(0, 0): grid[0][0]}
    parent = {(0, 0): None}

    directions = [(0, 1), (1, 0)]

    while heap:
        cost, i, j = heapq.heappop(heap)

        if (i, j) == end:
            break

        for ni, nj in directions:
            di, dj = i + ni, j + nj
            if 0 <= di < m and 0 <= dj < n:
                new_cost = cost + grid[di][dj]
                if (di, dj) not in costd or new_cost < costd[(ni, nj)]:
                    costd[(di, dj)] = new_cost
                    parent[(di, dj)] = (i, j)
                    heapq.heappush(heap, (new_cost, di, dj))

    path = []
    node = end
    while node:
        i, j = node
        path.append(grid[i][j])
        node = parent[node]
    
    return costd[end], path[::-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

min_cost, path = dijkstra_min_path(grid)
print("Minimum Path Sum:", min_cost)
print("Path:", path)
