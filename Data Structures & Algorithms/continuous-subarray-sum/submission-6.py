class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        cSum = nums[0]
        rmdrs = {0:-1, (cSum % k):0}
        for i in range(1, len(nums)):
            cSum += nums[i]

            rmdr = cSum % k
            print(rmdr, i - rmdrs[rmdr])
            if rmdr in rmdrs and i - rmdrs[rmdr] >= 2:
                return True

            if rmdr not in rmdrs:
                rmdrs[rmdr] = i

        return False

