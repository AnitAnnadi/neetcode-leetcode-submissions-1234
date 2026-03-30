class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            cSum = 0
            for j in range(i, n):
                cSum += nums[j]

                if cSum == k:
                    count += 1

        return count