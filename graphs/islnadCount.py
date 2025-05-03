def islandcount(grid):
        visited = set()
        count = 0

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                row, col = stack.pop()
                if (row, col) not in visited:
                    visited.add((row, col))
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_row, new_col = row + dr, col + dc
                        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 'L':
                            stack.append((new_row, new_col))
                            visited.add((row, col))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'L' and (r, c) not in visited:
                    dfs(r, c)
                    count += 1

        return count


if __name__ == "__main__":
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']
    ]
    print("Number of Islands:", islandcount(grid))  # Output: 4