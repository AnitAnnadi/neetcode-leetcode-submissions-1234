class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in diffs:
                nRow, nCol = r + dr, c + dc
                dfs(nRow, nCol)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res

