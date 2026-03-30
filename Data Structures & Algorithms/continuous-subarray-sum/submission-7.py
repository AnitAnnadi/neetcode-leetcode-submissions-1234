class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        cSum = 0
        rmdrs = {0:-1}
        for i in range(len(nums)):
            cSum += nums[i]

            rmdr = cSum % k
            if rmdr in rmdrs and i - rmdrs[rmdr] >= 2:
                return True

            if rmdr not in rmdrs:
                rmdrs[rmdr] = i

        return False

