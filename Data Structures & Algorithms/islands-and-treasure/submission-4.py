class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = 0
            
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                
                for dr, dc in diffs:
                    nRow = r + dr
                    nCol = c + dc

                    if min(nRow, nCol) < 0 or nRow >= ROWS or nCol >= COLS or grid[nRow][nCol] != 2147483647 or (nRow, nCol) in visited:
                        continue

                    q.append((nRow, nCol))
                    visited.add((nRow, nCol))

            dist += 1