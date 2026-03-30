class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        adj = {}
        visited = set()
        count = 0

        for course in range(numCourses):
            adj[course] = []

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        for course in range(numCourses):
            if not self.dst(course, adj, visited):
                return False

        return True
    
    def dst(self, course, adj, visited):
        if course in visited:
            return False
        
        if not adj[course]:
            return True
        
        visited.add(course)
        for pq in adj[course]:
            if not self.dst(pq, adj, visited):
                return False
        visited.remove(course)

        return True