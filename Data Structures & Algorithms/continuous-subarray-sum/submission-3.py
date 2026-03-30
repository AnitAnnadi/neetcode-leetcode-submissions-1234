class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        cSum = nums[0]
        rmdrs = {0, cSum % k}
        for i in range(1, len(nums)):
            cSum += nums[i]

            rmdr = cSum % k
            if rmdr in rmdrs and cSum >= k:
                return True

            rmdrs.add(rmdr)

        return False

