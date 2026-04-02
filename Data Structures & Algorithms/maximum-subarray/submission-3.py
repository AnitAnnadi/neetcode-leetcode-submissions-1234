class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = [0] * len(nums)
        s[0] = nums[0]

        for i in range(1, len(nums)):
            s[i] = nums[i] + max(0, s[i - 1])

        return max(s)