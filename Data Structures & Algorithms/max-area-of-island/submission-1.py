class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[0] * COLS for _ in range(ROWS)]
        maxCount = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and visited[r][c] != 1:
                    count = self.dfs(grid, visited, r, c)

                    if count > maxCount:
                        maxCount = count

        return maxCount
        
    def dfs(self, grid, visited, r, c):
        ROWS, COLS = len(grid), len(grid[0])

        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or visited[r][c] == 1:
            return 0
        
        count = 1
        visited[r][c] = 1

        count += self.dfs(grid, visited, r + 1, c)
        count += self.dfs(grid, visited, r - 1, c)
        count += self.dfs(grid, visited, r, c + 1)
        count += self.dfs(grid, visited, r, c - 1)

        return count
