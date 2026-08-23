class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        diffs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, coords):       
            coords.add((r, c))

            for dr, dc in diffs:
                nr, nc = r + dr, c + dc
                if nr == ROWS or nc == COLS or min(nr, nc) < 0 or (nr, nc) in coords or heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, coords)

        for i in range(ROWS):
            dfs(i, 0, pacific)
            dfs(i, COLS - 1, atlantic)

        for i in range(COLS):
            dfs(0, i, pacific)
            dfs(ROWS - 1, i, atlantic)

        return list(pacific & atlantic)
