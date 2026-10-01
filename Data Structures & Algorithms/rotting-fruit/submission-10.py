class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        numFresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numFresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if numFresh == 0:
            return 0

        res = 1
        diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in diffs:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue

                    numFresh -= 1
                    if numFresh == 0:
                        return res

                    grid[nr][nc] = 0
                    q.append((nr, nc))

            res += 1

        return -1
