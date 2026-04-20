class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []

        for num in arr:
            diff = abs(num - x)
            heapq.heappush(h, (-diff, -num))

            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for diff, num in h:
            res.append(-num)
        res.sort()

        return res