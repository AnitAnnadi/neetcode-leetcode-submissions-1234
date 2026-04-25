class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if r in rows and val in rows[r]:
                    return False
                else:
                    rows[r].add(val)
                
                if c in cols and val in cols[c]:
                    return False
                else:
                    cols[c].add(val)

                grid = (r // 3, c // 3)

                if grid in grids and val in grids[grid]:
                    return False
                else:
                    grids[grid].add(val)

        return True


