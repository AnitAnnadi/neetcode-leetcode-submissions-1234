class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        preSum = 0

        freq = defaultdict(int)
        freq[0] = 1
        for num in nums:
            preSum += num

            diff = preSum - k
            if diff in freq:
                total += freq[diff]
            
            freq[preSum] += 1
        
        return total
