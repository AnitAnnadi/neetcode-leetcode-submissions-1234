class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        cSum = nums[0]
        rmdrs = {0: -1, (cSum % k): 0 }
        for i in range(2, len(nums)):
            cSum += nums[i]

            rmdr = cSum % k
            if rmdr in rmdrs and rmdrs[rmdr] != i:
                print(rmdr, i)
                print(rmdrs)
                return True

            if rmdr not in rmdrs:
                rmdrs[rmdr] = i

        return False

