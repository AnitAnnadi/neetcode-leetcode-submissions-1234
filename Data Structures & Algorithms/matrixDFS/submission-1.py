class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        return self.dfs(grid, visited, 0, 0)
        
    def dfs(self, grid, visited, r, c):
        ROWS, COLS = len(grid), len(grid[0])

        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or visited[r][c] == 1:
            return 0
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        visited[r][c] = 1

        count = 0
        count += self.dfs(grid, visited, r + 1, c)
        count += self.dfs(grid, visited, r - 1, c)
        count += self.dfs(grid, visited, r, c + 1)
        count += self.dfs(grid, visited, r, c - 1)

        visited[r][c] = 0

        return count