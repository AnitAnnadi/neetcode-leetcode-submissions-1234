class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, l = 0, 0
        minLength = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minLength = min(minLength, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if minLength == float("inf") else minLength
