class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        minH = [(0, src)]
        shortest = {}

        while minH:
            w1, v1 = heapq.heappop(minH)
            if v1 in shortest:
                continue

            shortest[v1] = w1
            for v2, w2 in adj[v1]:
                if v2 in shortest:
                    continue

                heapq.heappush(minH, (w1 + w2, v2))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest