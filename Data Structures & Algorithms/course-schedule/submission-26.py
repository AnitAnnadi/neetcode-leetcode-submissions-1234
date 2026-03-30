class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        adj = {i: [] for i in range(numCourses)}
        taken = set()
        visited = set()

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        for course in range(numCourses):
            if not self.dst(course, adj, taken, visited):
                return False

        return True
    
    def dst(self, course, adj, taken, visited):
        if course in visited:
            return False

        if course in taken:
            return True
        
        if not adj[course]:
            taken.add(course)
            return True
        
        visited.add(course)
        for pq in adj[course]:
            if not self.dst(pq, adj, taken, visited):
                return False
            
        visited.remove(course)

        taken.add(course)
        return True