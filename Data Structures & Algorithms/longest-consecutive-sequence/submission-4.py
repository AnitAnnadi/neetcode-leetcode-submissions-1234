class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSeq = 0

        for num in nums:
            if (num - 1) not in numsSet:
                locSeq = 1
                while num + locSeq in numsSet:
                    locSeq += 1
                
                maxSeq = max(maxSeq, locSeq)

        return maxSeq

