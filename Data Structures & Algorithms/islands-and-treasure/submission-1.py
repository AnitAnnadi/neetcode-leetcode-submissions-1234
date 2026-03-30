class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            q = deque()
            visited = set()

            q.append((r, c))
            visited.add((r,c))

            dist = 0
            while q:
                for i in range(len(q)):
                    x, y = q.popleft()

                    if grid[x][y] == 0:
                        return dist
                
                    for dr, dc in diffs:
                        nRow = x + dr
                        nCol = y + dc

                        if min(nRow, nCol) < 0 or nRow >= ROWS or nCol >= COLS or grid[nRow][nCol] == -1 or (nRow, nCol) in visited:
                            continue

                        q.append((nRow, nCol))
                        visited.add((nRow, nCol))

                dist += 1
            
            return 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r, c)
