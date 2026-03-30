class MinHeap:
    
    def __init__(self):
        self.minHeap = [-1]

    def push(self, val: int) -> None:
        self.minHeap.append(val)

        curr = len(self.minHeap) - 1
        while curr > 1:
            parent = curr // 2
            if self.minHeap[curr] < self.minHeap[parent]:
                self.minHeap[curr], self.minHeap[parent] = self.minHeap[parent], self.minHeap[curr]
                curr = parent
            else:
                break

    def pop(self) -> int:
        if len(self.minHeap) == 1:
            return -1

        minVal = self.minHeap[1]
        self.minHeap[1] = self.minHeap[-1]
        self.minHeap.pop()
        self.heapifyDown(1)

        return minVal

    def top(self) -> int:
        if len(self.minHeap) == 1:
            return -1
        
        return self.minHeap[1]

    def heapify(self, nums: List[int]) -> None:
        self.minHeap = [-1] + nums

        curr = (len(self.minHeap) - 1) // 2
        while curr > 0:
            self.heapifyDown(curr)
            curr -= 1
    
    def heapifyDown(self, i):
        while 2 * i < len(self.minHeap):
            if 2 * i + 1 < len(self.minHeap) and self.minHeap[2 * i + 1] < self.minHeap[2 * i] and self.minHeap[2 * i + 1] < self.minHeap[i]:
                self.minHeap[i], self.minHeap[2 * i + 1] = self.minHeap[2 * i + 1], self.minHeap[i]
                i = 2 * i + 1
            elif self.minHeap[2 * i] < self.minHeap[i]:
                self.minHeap[i], self.minHeap[2 * i] = self.minHeap[2 * i], self.minHeap[i]
                i = 2 * i
            else:
                break
        
        