class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCounts = defaultdict(int)
        prefixCounts[0] += 1
        cSum, count = 0, 0

        for num in nums:
            cSum += num
            if (cSum - k) in prefixCounts:
                count += prefixCounts[cSum - k]
            
            prefixCounts[cSum] += 1

        return count