class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        cSum = nums[0]
        rmdrs = {0, cSum % k}
        for i in range(2, len(nums)):
            cSum += nums[i]

            rmdr = cSum % k
            if rmdr in rmdrs:
                return True

            if rmdr not in rmdrs:
                rmdrs[rmdr] = i

        return False

