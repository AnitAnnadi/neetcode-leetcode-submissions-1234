class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        res = []
        self.dfs(counts, len(nums), res, [])

        return res

    def dfs(self, counts, nLen, res, perm):
        if len(perm) == nLen:
            res.append(perm.copy())
            return

        for c in counts:
            if counts[c] > 0:
                counts[c] -= 1
                perm.append(c)

                self.dfs(counts, nLen, res, perm)

                counts[c] += 1
                perm.pop()
                