class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            total += num

        leftSum = 0
        for i in range(0, len(nums)):
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i

            leftSum += nums[i]
        
        return -1
