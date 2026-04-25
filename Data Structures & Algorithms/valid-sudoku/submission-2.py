class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vals = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                grid = (r // 3, c // 3)
                if val in vals[("r", r)] or val in vals[("c", c)] or val in vals[("g", grid)]:
                    return False
                
                vals[("r", r)].add(val)
                vals[("c", c)].add(val)
                vals[("g", grid)].add(val)

        return True


