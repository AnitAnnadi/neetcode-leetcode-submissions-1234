class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        limit = len(nums) // 3
        res = []
        for num, count in counts.items():
            if count > limit:
                res.append(num)

        return res
