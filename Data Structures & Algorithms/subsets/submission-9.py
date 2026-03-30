class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.subsetsHelper(nums, res, 0, [])

        return res

    def subsetsHelper(self, nums, res, i, currSet):
        if i >= len(nums):
            res.append(currSet.copy())
            return

        currSet.append(nums[i])
        self.subsetsHelper(nums, res, i + 1, currSet)
        currSet.pop()

        self.subsetsHelper(nums, res, i + 1, currSet)