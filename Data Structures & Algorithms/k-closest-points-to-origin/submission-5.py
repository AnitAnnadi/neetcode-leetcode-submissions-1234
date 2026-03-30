class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-(point[0] ** 2 + point[1] ** 2), point) for point in points]
        maxHeap = []

        for point in points:
            heapq.heappush(maxHeap, point)

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            res.append(maxHeap[0][1])
            heapq.heappop(maxHeap)
        
        return res
