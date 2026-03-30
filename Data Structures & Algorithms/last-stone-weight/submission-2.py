class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = maxHeap[0]
            heapq.heappop(maxHeap)
            y = maxHeap[0]
            heapq.heappop(maxHeap)

            if (x != y):
                heapq.heappush(maxHeap, x - y)
    
        return 0 if len(maxHeap) == 0 else -maxHeap[0]
        

