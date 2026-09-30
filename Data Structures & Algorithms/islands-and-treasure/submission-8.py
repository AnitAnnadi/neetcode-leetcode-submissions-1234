class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 1
        diffs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in diffs:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 2147483647:
                        continue

                    grid[nr][nc] = dist
                    q.append((nr, nc))

            dist += 1