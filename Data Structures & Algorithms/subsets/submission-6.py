class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subsetHelper(nums, res, [], 0)

        return res

        
    def subsetHelper(self, nums, res, currArr, i):
        if i >= len(nums):
            res.append(currArr[:])
            return

        currArr.append(nums[i])
        self.subsetHelper(nums, res, currArr, i + 1)
        currArr.pop()
        self.subsetHelper(nums, res, currArr, i + 1)