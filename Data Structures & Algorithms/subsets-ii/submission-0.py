class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.subsetsWithDupHelper(nums, res, [], 0)

        return res
    
    def subsetsWithDupHelper(self, nums, res, currArr, i):
        if i >= len(nums):
            res.append(currArr.copy())
            return

        currArr.append(nums[i])
        self.subsetsWithDupHelper(nums, res, currArr, i + 1)
        currArr.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.subsetsWithDupHelper(nums, res, currArr, i + 1)


