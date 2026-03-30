class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        trips.sort(key = lambda x: x[1])

        currPass = 0
        for numPass, s, e in trips:
            while minHeap and minHeap[0][0] <= s:
                currPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            currPass += numPass
            if currPass > capacity:
                return False

            heapq.heappush(minHeap, (e, numPass))
        
        return True



