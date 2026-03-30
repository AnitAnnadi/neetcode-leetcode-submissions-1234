class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
        heapq.heapify(points)
        

        res = []
        for i in range(k):
            res.append(points[0][1])
            heapq.heappop(points)
        
        return res
