class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqs = defaultdict(list)
        for crs1, crs2 in prerequisites:
            preReqs[crs1].append(crs2)

        visited, taken, res = set(), set(), []
        def dfs(crs):
            if crs in visited:
                return False
            
            if crs in taken:
                return True

            visited.add(crs)
            for pq in preReqs[crs]:
                if not dfs(pq):
                    return False
            visited.remove(crs)

            taken.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
