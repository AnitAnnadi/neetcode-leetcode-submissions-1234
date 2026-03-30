class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        
        if dst not in self.graph:
            self.graph[dst] = set()

        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        q = deque()
        q.append(src)

        while q:
            for i in range(len(q)):
                v = q.popleft()

                if v == dst:
                    return True
                
                for e in self.graph[v]:
                    if e in visited:
                        continue

                    q.append(e)
                    visited.add(e)
        
        return False

