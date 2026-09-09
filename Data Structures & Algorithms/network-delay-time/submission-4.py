class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        minH = [(0, k)]
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

        for i in range(1, n + 1):
            if i not in shortest:
                return -1

        return max(shortest.values())