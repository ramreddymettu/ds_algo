## Tekion Interview 
import heapq

def dijkstra_min_path(grid):
    if not grid or not grid[0]:
        return 0, []

    m, n = len(grid), len(grid[0])
    start = (0, 0)
    end = (m - 1, n - 1)
    print(f"Start - {start} \n End - {end}")

    # Priority queue: (cost, i, j)
    heap = [(grid[0][0], 0, 0)]
    # Store minimum cost to reach each cell
    cost = {(0, 0): grid[0][0]}
    # To reconstruct path
    parent = {(0, 0): None}

    directions = [(0, 1), (1, 0)]  # Right and Down

    while heap:
        curr_cost, i, j = heapq.heappop(heap)

        if (i, j) == end:
            break

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                new_cost = curr_cost + grid[ni][nj]
                if (ni, nj) not in cost or new_cost < cost[(ni, nj)]:
                    cost[(ni, nj)] = new_cost
                    parent[(ni, nj)] = (i, j)
                    heapq.heappush(heap, (new_cost, ni, nj))
                    print(f"Cost - {cost} \n Parent - {parent} \n Heaq - {heap}")
                    print("*********************")

    # Reconstruct path from end to start
    path = []
    node = end
    while node:
        i, j = node
        path.append(grid[i][j])
        node = parent[node]

    return cost[end], path[::-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

min_cost, path = dijkstra_min_path(grid)
print("Minimum Path Sum:", min_cost)
print("Path:", path)
