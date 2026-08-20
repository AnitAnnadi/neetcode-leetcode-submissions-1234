class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))

        minHeap = [(0, src)]

        shortest = {}
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 in shortest:
                    continue

                heapq.heappush(minHeap, (w1 + w2, n2))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


