class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        trips.sort(key = lambda x: x[1])

        currPassengers = 0
        for passengers, s, e in trips:
            while h and h[0][0] <= s:
                trip = heapq.heappop(h)
                currPassengers -= trip[1]
            
            currPassengers += passengers
            if currPassengers > capacity:
                return False

            heapq.heappush(h, (e, passengers))
        
        return True



