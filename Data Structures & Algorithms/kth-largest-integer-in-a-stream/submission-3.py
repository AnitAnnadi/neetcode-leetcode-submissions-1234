class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []

        for num in nums:
            heapq.heappush(self.h, num)

            if len(self.h) > k:
                heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        heapq.heappop(self.h)

        return self.h[0]
