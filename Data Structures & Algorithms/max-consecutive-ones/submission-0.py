class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currCount = 0

        for num in nums:
            if num == 1:
                currCount += 1
                maxCount = max(maxCount, currCount)
            else:
                currCount = 0

        return maxCount