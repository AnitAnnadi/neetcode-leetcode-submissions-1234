class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        total = 0

        for num in nums:
            total += num

        leftSum = 0
        for i in range(0, len(nums)):
            if leftSum == (total - leftSum - nums[i]):
                return i

            leftSum += nums[i]
        
        return -1
