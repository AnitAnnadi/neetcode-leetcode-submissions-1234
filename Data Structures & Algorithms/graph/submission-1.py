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
        return self.dst(src, dst)
    
    def dst(self, src, dst):
        if src == dst:
            return True

        for v in self.graph[src]:
            if self.dst(v, dst):
                return True
        
        return False

