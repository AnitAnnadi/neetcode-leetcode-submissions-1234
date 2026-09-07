class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freqs = [[] for _ in range(len(nums))]
        res = []

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            freqs[count - 1].append(num)

        i = len(nums) - 1
        while k > 0:
            for num in freqs[i]:
                res.append(num)
                k -= 1
            
            i -= 1

        return res