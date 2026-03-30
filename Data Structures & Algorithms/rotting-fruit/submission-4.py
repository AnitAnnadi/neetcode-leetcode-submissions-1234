class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        length = 1
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        if fresh == 0:
            return 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nRow, nCol = r + dr, c + dc

                    if min(nRow, nCol) < 0 or nRow == ROWS or nCol == COLS or grid[nRow][nCol] != 1:
                        continue
                    
                    q.append([nRow, nCol])
                    fresh -= 1
                    grid[nRow][nCol] = 2

                    if fresh == 0:
                        return length
            
            length += 1
        
        return -1
        

                
        
