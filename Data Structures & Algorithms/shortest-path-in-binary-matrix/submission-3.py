class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        length = 1
        q = deque()
        visited = [[0] * COLS for _ in range(ROWS)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1]]

        if grid[0][0] == 0:
            q.append([0, 0])
            visited[0][0] = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 or c == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    nRow, nCol = r + dr, c + dc
                    
                    if min(nRow, nCol) < 0 or nRow == ROWS or nCol == COLS or grid[nRow][nCol] == 1 or visited[nRow][nCol] == 1:
                        continue
                    
                    q.append([nRow, nCol])
                    visited[nRow][nCol] = 1
        
            length += 1
        
        return -1