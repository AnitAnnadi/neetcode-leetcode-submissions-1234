class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        newCounts = defaultdict(list)
        for c in counts:
            newCounts[counts[c]].append(c)

        res = []
        for i in range(len(nums), 0, -1):
            if i in newCounts:
                for j in newCounts[i]:
                    res.append(j)
                    k -= 1

                    if k == 0:
                        return res

