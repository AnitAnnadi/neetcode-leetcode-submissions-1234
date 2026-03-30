class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        self.dfs(nums, used, res, [])
        return res

    def dfs(self, nums, used, res, perm):
        if len(perm) == len(nums):
            res.append(perm.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                perm.append(nums[i])
                used[i] = True

                self.dfs(nums, used, res, perm)

                perm.pop()
                used[i] = False


