class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        for stone in stones:
            heapq.heappush(h, -stone)
        
        while len(h) > 1:
            y = heapq.heappop(h)
            x = heapq.heappop(h)

            if x == y:
                continue
            else:
                heapq.heappush(h, y - x)
        
        return 0 if len(h) == 0 else -h[0]