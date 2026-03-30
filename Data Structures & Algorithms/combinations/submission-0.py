class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.combineHelper(n, k, res, [], 1)

        return res

    def combineHelper(self, n, k, res, currArr, i):
        if len(currArr) == k:
            res.append(currArr.copy())
            return
        
        if i > n:
            return

        currArr.append(i)
        self.combineHelper(n, k, res, currArr, i + 1)
        currArr.pop()

        self.combineHelper(n, k, res, currArr, i + 1)