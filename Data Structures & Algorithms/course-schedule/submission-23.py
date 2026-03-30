class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return numCourses

        adj = {}
        visited = set()
        count = 0

        for src, dst in prerequisites:
            if src not in adj:
                adj[src] = []

            if dst not in adj:
                adj[dst] = []

            adj[src].append(dst)
        
        for course in range(numCourses):
            count += self.dst(course, adj, visited)

        return count == numCourses
    
    def dst(self, course, adj, visited):
        if course in visited:
            return 0

        if not adj[course]:
            return 1
        
        count = 0
        visited.add(course)
        for pq in adj[course]:
            count += self.dst(pq, adj, visited)
        
        return count