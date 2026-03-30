class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        rCounts = {value: key for key, value in counts.items()}

        res = []
        for i in range(len(nums), 0, -1):
            if i in rCounts:
                res.append(rCounts[i])
                k -= 1
            
                if k == 0:
                    break

        return res

