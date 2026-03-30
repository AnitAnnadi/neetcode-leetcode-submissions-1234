class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        self.combinationSumHelper(nums, target, res, 0, [], 0)
        return res
    
    def combinationSumHelper(self, nums, target, res, currSum, currArr, i):

        if currSum == target:
            res.append(currArr[:])
            return
        
        if currSum > target:
            return
        
        for j in range(i, len(nums)):
            currArr.append(nums[j])
            self.combinationSumHelper(nums, target, res, currSum + nums[j], currArr, j)
            currArr.pop()