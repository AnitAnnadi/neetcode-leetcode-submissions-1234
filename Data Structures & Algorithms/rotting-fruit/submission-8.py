class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        numFresh = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    numFresh += 1
        
        if numFresh == 0:
            return 0

        diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        mins = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in diffs:
                    nRow = r + dr
                    nCol = c + dc

                    if min(nRow, nCol) < 0 or nRow == ROWS or nCol == COLS or grid[nRow][nCol] != 1:
                        continue
                    
                    numFresh -= 1
                    if numFresh == 0:
                        return mins
                    
                    grid[nRow][nCol] = 2
                    q.append((nRow, nCol))

            mins += 1

        return -1
            
