class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.combinationSumHelper(nums, target, res, [], 0, 0)

        return res

    def combinationSumHelper(self, nums, target, res, currArr, currSum, i):
        if currSum == target:
            res.append(currArr.copy())
            return

        if currSum > target or i >= len(nums):
            return

        for j in range(i, len(nums)):
            currArr.append(nums[j])
            self.combinationSumHelper(nums, target, res, currArr, currSum + nums[j], j)
            currArr.pop()